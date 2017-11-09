import re
import logging
import collections
import functools
import subprocess

from antlr.JavaParserListener import JavaParserListener
from antlr.JavaLexer import JavaLexer
from antlr.JavaParser import JavaParser

from agents.Refactor import Refactor

def IsJavaMethodInvocationOrConst(token):
  if (type(token) == JavaParser.StatementContext
      and token.getText().endswith(');')):
    return True
  return False

def IsJavaMethodInvocationOrConstWithName(token, name):
  return IsJavaMethodInvocationOrConst(token) and name+'(' in token.getText()

def GetIsJavaMcFn(name):
  def _inner_fn(token):
    return IsJavaMethodInvocationOrConstWithName(token, name)
  return _inner_fn

class JavaAgentBase(JavaParserListener):
  @staticmethod
  def createLexer(input_stream):
    return JavaLexer(input_stream)

  @staticmethod
  def createParser(token_stream):
    return JavaParser(token_stream)

  @staticmethod
  def defaultEntryPoint(parser):
    return parser.compilationUnit()

  @staticmethod
  def addOptions(parser):
    return parser

  def __init__(self):
    self._filepath = None

  @property
  def args(self):
    return self._args

  @property
  def filepath(self):
    return self._filepath

  def skip(self, filename):
    if not filename.endswith('.java'):
      logging.info('This is not a java file')
      return True
    return False

  def set_file(self, filepath):
    self._filepath = filepath

  def __init__(self, args):
    self._args =  args

  #Override
  def actions(self):
    """Implement this to define the actions needed for a Java refactoring"""
    raise NotImplementedError("actions not implemented")

  #Override
  def validate(self):
    raise NotImplementedError("validate not implemented")

  #Override
  def clean(self):
    raise NotImplementedError("clean not implemented")

  #Override
  def setup(self):
    raise NotImplementedError("setup not implemented")

class JavaRefactorAgent(JavaAgentBase):
  @staticmethod
  def addOptions(parser):
    return parser

  def __init__(self, args):
    self._element_list = []
    super(JavaRefactorAgent, self).__init__(args)
    self._element_table = collections.defaultdict(list)
    self._imported_packages = []
    self._class_name = None
    self._refactor = None

  @property
  def ls(self):
    return self._element_list

  @property
  def tb(self):
    return self._element_table

  @property
  def refactor(self):
    return self._refactor

  @property
  def start_mask(self):
    return '/*SAUL:*/ '

  @property
  def end_mask(self):
    return ' /*:SAUL*/'

  @property
  def class_name(self):
    return self._class_name

  #Override
  def clean(self):
    sed_string = 's/%s.*%s//g' % (
        re.escape(self.start_mask), re.escape(self.end_mask))
    if self.args.file:
      subprocess.call(['sed', '-i', sed_string, self.args.file])
    else:
      subprocess.call(['find', self.args.directory, '-type', 'f', '-exec',
                       'sed', '-i', sed_string, '{}', ';'])

  #Override
  def set_file(self, filepath):
    self._filepath = filepath
    self._refactor = Refactor(filepath, self.args.save_as_new,
        start_mask=self.start_mask, end_mask=self.end_mask)

  #Override
  def setup(self):
    self._element_list = sorted(self.ls, key=lambda x: x.start.start)
    for i in self.ls:
      self._element_table[type(i)].append(i)
    main_class_context = functools.reduce(
        (lambda x,y: x if x.depth() < y.depth() else y),
        self._element_table[JavaParser.ClassDeclarationContext])
    self._class_name = main_class_context.IDENTIFIER().getText()

  #Override
  def actions(self):
    """Implement this to define the actions needed for a Java refactoring"""
    raise NotImplementedError("actions not implemented")

  def addImport(self, package_name):
    if package_name.endswith(';'):
      package_name = package_name[:-1]
    if package_name not in self._imported_packages:
      insertion = 'import %s;' % package_name
      imports = self.refactor.actionOnX(
          self.tb, JavaParser.ImportDeclarationContext)
      self.refactor.insertAfterToken(imports[-1], insertion, use_mask=True)
      self._imported_packages.append(package_name)

  def reset(self):
    self._element_list = []
    self._element_table = collections.defaultdict(list)

  ##### Overriding exit token methods for parser listener #####
  def exitCompilationUnit(self, ctx):
    self.ls.append(ctx)

  def exitPackageDeclaration(self, ctx):
    self.ls.append(ctx)

  def exitImportDeclaration(self, ctx):
    self.ls.append(ctx)

  def exitTypeDeclaration(self, ctx):
    self.ls.append(ctx)

  def exitModifier(self, ctx):
    self.ls.append(ctx)

  def exitClassOrInterfaceModifier(self, ctx):
    self.ls.append(ctx)

  def exitVariableModifier(self, ctx):
    self.ls.append(ctx)

  def exitClassDeclaration(self, ctx):
    self.ls.append(ctx)

  def exitTypeParameters(self, ctx):
    self.ls.append(ctx)

  def exitTypeParameter(self, ctx):
    self.ls.append(ctx)

  def exitTypeBound(self, ctx):
    self.ls.append(ctx)

  def exitEnumDeclaration(self, ctx):
    self.ls.append(ctx)

  def exitEnumConstants(self, ctx):
    self.ls.append(ctx)

  def exitEnumConstant(self, ctx):
    self.ls.append(ctx)

  def exitEnumBodyDeclarations(self, ctx):
    self.ls.append(ctx)

  def exitInterfaceDeclaration(self, ctx):
    self.ls.append(ctx)

  def exitClassBody(self, ctx):
    self.ls.append(ctx)

  def exitInterfaceBody(self, ctx):
    self.ls.append(ctx)

  def exitClassBodyDeclaration(self, ctx):
    self.ls.append(ctx)

  def exitMemberDeclaration(self, ctx):
    self.ls.append(ctx)

  def exitMethodDeclaration(self, ctx):
    self.ls.append(ctx)

  def exitMethodBody(self, ctx):
    self.ls.append(ctx)

  def exitTypeTypeOrVoid(self, ctx):
    self.ls.append(ctx)

  def exitGenericMethodDeclaration(self, ctx):
    self.ls.append(ctx)

  def exitGenericConstructorDeclaration(self, ctx):
    self.ls.append(ctx)

  def exitConstructorDeclaration(self, ctx):
    self.ls.append(ctx)

  def exitFieldDeclaration(self, ctx):
    self.ls.append(ctx)

  def exitInterfaceBodyDeclaration(self, ctx):
    self.ls.append(ctx)

  def exitInterfaceMemberDeclaration(self, ctx):
    self.ls.append(ctx)

  def exitConstDeclaration(self, ctx):
    self.ls.append(ctx)

  def exitConstantDeclarator(self, ctx):
    self.ls.append(ctx)

  def exitInterfaceMethodDeclaration(self, ctx):
    self.ls.append(ctx)

  def exitInterfaceMethodModifier(self, ctx):
    self.ls.append(ctx)

  def exitGenericInterfaceMethodDeclaration(self, ctx):
    self.ls.append(ctx)

  def exitVariableDeclarators(self, ctx):
    self.ls.append(ctx)

  def exitVariableDeclarator(self, ctx):
    self.ls.append(ctx)

  def exitVariableDeclaratorId(self, ctx):
    self.ls.append(ctx)

  def exitVariableInitializer(self, ctx):
    self.ls.append(ctx)

  def exitArrayInitializer(self, ctx):
    self.ls.append(ctx)

  def exitClassOrInterfaceType(self, ctx):
    self.ls.append(ctx)

  def exitTypeArgument(self, ctx):
    self.ls.append(ctx)

  def exitQualifiedNameList(self, ctx):
    self.ls.append(ctx)

  def exitFormalParameters(self, ctx):
    self.ls.append(ctx)

  def exitFormalParameterList(self, ctx):
    self.ls.append(ctx)

  def exitFormalParameter(self, ctx):
    self.ls.append(ctx)

  def exitLastFormalParameter(self, ctx):
    self.ls.append(ctx)

  def exitQualifiedName(self, ctx):
    self.ls.append(ctx)

  def exitLiteral(self, ctx):
    self.ls.append(ctx)

  def exitIntegerLiteral(self, ctx):
    self.ls.append(ctx)

  def exitFloatLiteral(self, ctx):
    self.ls.append(ctx)

  def exitAnnotation(self, ctx):
    self.ls.append(ctx)

  def exitElementValuePairs(self, ctx):
    self.ls.append(ctx)

  def exitElementValuePair(self, ctx):
    self.ls.append(ctx)

  def exitElementValue(self, ctx):
    self.ls.append(ctx)

  def exitElementValueArrayInitializer(self, ctx):
    self.ls.append(ctx)

  def exitAnnotationTypeDeclaration(self, ctx):
    self.ls.append(ctx)

  def exitAnnotationTypeBody(self, ctx):
    self.ls.append(ctx)

  def exitAnnotationTypeElementDeclaration(self, ctx):
    self.ls.append(ctx)

  def exitAnnotationTypeElementRest(self, ctx):
    self.ls.append(ctx)

  def exitAnnotationMethodOrConstantRest(self, ctx):
    self.ls.append(ctx)

  def exitAnnotationMethodRest(self, ctx):
    self.ls.append(ctx)

  def exitAnnotationConstantRest(self, ctx):
    self.ls.append(ctx)

  def exitDefaultValue(self, ctx):
    self.ls.append(ctx)

  def exitBlock(self, ctx):
    self.ls.append(ctx)

  def exitBlockStatement(self, ctx):
    self.ls.append(ctx)

  def exitLocalVariableDeclaration(self, ctx):
    self.ls.append(ctx)

  def exitLocalTypeDeclaration(self, ctx):
    self.ls.append(ctx)

  def exitStatement(self, ctx):
    self.ls.append(ctx)

  def exitCatchClause(self, ctx):
    self.ls.append(ctx)

  def exitCatchType(self, ctx):
    self.ls.append(ctx)

  def exitFinallyBlock(self, ctx):
    self.ls.append(ctx)

  def exitResourceSpecification(self, ctx):
    self.ls.append(ctx)

  def exitResources(self, ctx):
    self.ls.append(ctx)

  def exitResource(self, ctx):
    self.ls.append(ctx)

  def exitSwitchBlockStatementGroup(self, ctx):
    self.ls.append(ctx)

  def exitSwitchLabel(self, ctx):
    self.ls.append(ctx)

  def exitForControl(self, ctx):
    self.ls.append(ctx)

  def exitForInit(self, ctx):
    self.ls.append(ctx)

  def exitEnhancedForControl(self, ctx):
    self.ls.append(ctx)

  def exitParExpression(self, ctx):
    self.ls.append(ctx)

  def exitExpressionList(self, ctx):
    self.ls.append(ctx)

  def exitExpression(self, ctx):
    self.ls.append(ctx)

  def exitLambdaExpression(self, ctx):
    self.ls.append(ctx)

  def exitLambdaParameters(self, ctx):
    self.ls.append(ctx)

  def exitLambdaBody(self, ctx):
    self.ls.append(ctx)

  def exitPrimary(self, ctx):
    self.ls.append(ctx)

  def exitClassType(self, ctx):
    self.ls.append(ctx)

  def exitCreator(self, ctx):
    self.ls.append(ctx)

  def exitCreatedName(self, ctx):
    self.ls.append(ctx)

  def exitInnerCreator(self, ctx):
    self.ls.append(ctx)

  def exitArrayCreatorRest(self, ctx):
    self.ls.append(ctx)

  def exitClassCreatorRest(self, ctx):
    self.ls.append(ctx)

  def exitExplicitGenericInvocation(self, ctx):
    self.ls.append(ctx)

  def exitTypeArgumentsOrDiamond(self, ctx):
    self.ls.append(ctx)

  def exitNonWildcardTypeArgumentsOrDiamond(self, ctx):
    self.ls.append(ctx)

  def exitNonWildcardTypeArguments(self, ctx):
    self.ls.append(ctx)

  def exitTypeList(self, ctx):
    self.ls.append(ctx)

  def exitTypeType(self, ctx):
    self.ls.append(ctx)

  def exitPrimitiveType(self, ctx):
    self.ls.append(ctx)

  def exitTypeArguments(self, ctx):
    self.ls.append(ctx)

  def exitSuperSuffix(self, ctx):
    self.ls.append(ctx)

  def exitExplicitGenericInvocationSuffix(self, ctx):
    self.ls.append(ctx)

  def exitArguments(self, ctx):
    self.ls.append(ctx)
