import logging
import collections

from antlr.JavaParserListener import JavaParserListener
from antlr.JavaLexer import JavaLexer
from antlr.JavaParser import JavaParser

from agents.Refactor import Refactor

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

  def actions(self):
    """Implement this to define the actions needed for a Java refactoring"""
    raise NotImplementedError("actions not implemented")


class JavaRefactorAgent(JavaAgentBase):
  @staticmethod
  def addOptions(parser):
    return parser

  @property
  def ls(self):
    return self._element_list

  @property
  def tb(self):
    return self._element_table

  @property
  def refactor(self):
    return self._refactor

  def __init__(self, args):
    self._element_list = []
    self._element_table = collections.defaultdict(list)
    super(JavaRefactorAgent, self).__init__()

  #Override
  def set_file(self, filepath):
    self._filepath = filepath
    self._refactor = Refactor(filepath, self.args.save_as_new)

  def reset(self):
    self._element_list = []
    self._element_table = collections.defaultdict(list)

  #Override
  def actions(self):
    """Implement this to define the actions needed for a Java refactoring"""
    raise NotImplementedError("actions not implemented")

  ##### Overriding exit token methods for parser listener #####
  def exitCompilationUnit(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitPackageDeclaration(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitImportDeclaration(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitTypeDeclaration(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitModifier(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitClassOrInterfaceModifier(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitVariableModifier(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitClassDeclaration(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitTypeParameters(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitTypeParameter(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitTypeBound(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitEnumDeclaration(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitEnumConstants(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitEnumConstant(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitEnumBodyDeclarations(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitInterfaceDeclaration(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitClassBody(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitInterfaceBody(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitClassBodyDeclaration(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitMemberDeclaration(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitMethodDeclaration(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitMethodBody(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitTypeTypeOrVoid(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitGenericMethodDeclaration(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitGenericConstructorDeclaration(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitConstructorDeclaration(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitFieldDeclaration(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitInterfaceBodyDeclaration(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitInterfaceMemberDeclaration(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitConstDeclaration(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitConstantDeclarator(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitInterfaceMethodDeclaration(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitInterfaceMethodModifier(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitGenericInterfaceMethodDeclaration(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitVariableDeclarators(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitVariableDeclarator(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitVariableDeclaratorId(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitVariableInitializer(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitArrayInitializer(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitClassOrInterfaceType(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitTypeArgument(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitQualifiedNameList(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitFormalParameters(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitFormalParameterList(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitFormalParameter(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitLastFormalParameter(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitQualifiedName(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitLiteral(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitIntegerLiteral(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitFloatLiteral(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitAnnotation(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitElementValuePairs(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitElementValuePair(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitElementValue(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitElementValueArrayInitializer(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitAnnotationTypeDeclaration(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitAnnotationTypeBody(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitAnnotationTypeElementDeclaration(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitAnnotationTypeElementRest(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitAnnotationMethodOrConstantRest(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitAnnotationMethodRest(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitAnnotationConstantRest(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitDefaultValue(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitBlock(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitBlockStatement(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitLocalVariableDeclaration(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitLocalTypeDeclaration(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitStatement(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitCatchClause(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitCatchType(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitFinallyBlock(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitResourceSpecification(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitResources(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitResource(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitSwitchBlockStatementGroup(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitSwitchLabel(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitForControl(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitForInit(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitEnhancedForControl(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitParExpression(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitExpressionList(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitExpression(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitLambdaExpression(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitLambdaParameters(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitLambdaBody(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitPrimary(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitClassType(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitCreator(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitCreatedName(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitInnerCreator(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitArrayCreatorRest(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitClassCreatorRest(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitExplicitGenericInvocation(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitTypeArgumentsOrDiamond(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitNonWildcardTypeArgumentsOrDiamond(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitNonWildcardTypeArguments(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitTypeList(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitTypeType(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitPrimitiveType(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitTypeArguments(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitSuperSuffix(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitExplicitGenericInvocationSuffix(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)

  def exitArguments(self, ctx):
    self.tb[type(ctx)].append(ctx)
    self.ls.append(ctx)
