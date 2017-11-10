import re
import logging
import collections
import functools
import subprocess

from antlr.CPP14Listener import CPP14Listener
from antlr.CPP14Lexer import CPP14Lexer
from antlr.CPP14Parser import CPP14Parser

from agents.Refactor import Refactor

class CppAgentBase(CPP14Listener):
  @staticmethod
  def createLexer(input_stream):
    return CPP14Lexer(input_stream)

  @staticmethod
  def createParser(token_stream):
    return CPP14Parser(token_stream)

  @staticmethod
  def defaultEntryPoint(parser):
    import ipdb
    ipdb.set_trace()
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
    if not filename.endswith('.cc') or not filename.endswith('.h'):
      logging.info('This is not a java file')
      return True
    return False

  def set_file(self, filepath):
    self._filepath = filepath

  def __init__(self, args):
    self._args =  args

  #Override
  def actions(self):
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

class CppRefactorAgent(CppAgentBase):
  @staticmethod
  def addOptions(parser):
    return parser

  def __init__(self, args):
    self._element_list = []
    super(CppRefactorAgent, self).__init__(args)
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
#     main_class_context = functools.reduce(
        # (lambda x,y: x if x.depth() < y.depth() else y),
        # self._element_table[CppParser.ClassDeclarationContext])
    #self._class_name = main_class_context.IDENTIFIER().getText()

  #Override
  def actions(self):
    """Implement this to define the actions needed for a Cpp refactoring"""
    raise NotImplementedError("actions not implemented")

  def addImport(self, package_name):
    pass
#     if package_name.endswith(';'):
      # package_name = package_name[:-1]
    # if package_name not in self._imported_packages:
      # insertion = 'import %s;' % package_name
      # imports = self.refactor.actionOnX(
          # self.tb, CppParser.ImportDeclarationContext)
      # self.refactor.insertAfterToken(imports[-1], insertion, use_mask=True)
      # self._imported_packages.append(package_name)

  def reset(self):
    self._element_list = []
    self._element_table = collections.defaultdict(list)

  ##### Overriding exit token methods for parser listener #####
  # Enter a parse tree produced by CPP14Parser#translationunit.
  def enterTranslationunit(self, ctx:CPP14Parser.TranslationunitContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#translationunit.
  def exitTranslationunit(self, ctx:CPP14Parser.TranslationunitContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#primaryexpression.
  def enterPrimaryexpression(self, ctx:CPP14Parser.PrimaryexpressionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#primaryexpression.
  def exitPrimaryexpression(self, ctx:CPP14Parser.PrimaryexpressionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#idexpression.
  def enterIdexpression(self, ctx:CPP14Parser.IdexpressionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#idexpression.
  def exitIdexpression(self, ctx:CPP14Parser.IdexpressionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#unqualifiedid.
  def enterUnqualifiedid(self, ctx:CPP14Parser.UnqualifiedidContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#unqualifiedid.
  def exitUnqualifiedid(self, ctx:CPP14Parser.UnqualifiedidContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#qualifiedid.
  def enterQualifiedid(self, ctx:CPP14Parser.QualifiedidContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#qualifiedid.
  def exitQualifiedid(self, ctx:CPP14Parser.QualifiedidContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#nestednamespecifier.
  def enterNestednamespecifier(self, ctx:CPP14Parser.NestednamespecifierContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#nestednamespecifier.
  def exitNestednamespecifier(self, ctx:CPP14Parser.NestednamespecifierContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#lambdaexpression.
  def enterLambdaexpression(self, ctx:CPP14Parser.LambdaexpressionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#lambdaexpression.
  def exitLambdaexpression(self, ctx:CPP14Parser.LambdaexpressionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#lambdaintroducer.
  def enterLambdaintroducer(self, ctx:CPP14Parser.LambdaintroducerContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#lambdaintroducer.
  def exitLambdaintroducer(self, ctx:CPP14Parser.LambdaintroducerContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#lambdacapture.
  def enterLambdacapture(self, ctx:CPP14Parser.LambdacaptureContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#lambdacapture.
  def exitLambdacapture(self, ctx:CPP14Parser.LambdacaptureContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#capturedefault.
  def enterCapturedefault(self, ctx:CPP14Parser.CapturedefaultContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#capturedefault.
  def exitCapturedefault(self, ctx:CPP14Parser.CapturedefaultContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#capturelist.
  def enterCapturelist(self, ctx:CPP14Parser.CapturelistContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#capturelist.
  def exitCapturelist(self, ctx:CPP14Parser.CapturelistContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#capture.
  def enterCapture(self, ctx:CPP14Parser.CaptureContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#capture.
  def exitCapture(self, ctx:CPP14Parser.CaptureContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#simplecapture.
  def enterSimplecapture(self, ctx:CPP14Parser.SimplecaptureContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#simplecapture.
  def exitSimplecapture(self, ctx:CPP14Parser.SimplecaptureContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#initcapture.
  def enterInitcapture(self, ctx:CPP14Parser.InitcaptureContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#initcapture.
  def exitInitcapture(self, ctx:CPP14Parser.InitcaptureContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#lambdadeclarator.
  def enterLambdadeclarator(self, ctx:CPP14Parser.LambdadeclaratorContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#lambdadeclarator.
  def exitLambdadeclarator(self, ctx:CPP14Parser.LambdadeclaratorContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#postfixexpression.
  def enterPostfixexpression(self, ctx:CPP14Parser.PostfixexpressionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#postfixexpression.
  def exitPostfixexpression(self, ctx:CPP14Parser.PostfixexpressionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#expressionlist.
  def enterExpressionlist(self, ctx:CPP14Parser.ExpressionlistContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#expressionlist.
  def exitExpressionlist(self, ctx:CPP14Parser.ExpressionlistContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#pseudodestructorname.
  def enterPseudodestructorname(self, ctx:CPP14Parser.PseudodestructornameContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#pseudodestructorname.
  def exitPseudodestructorname(self, ctx:CPP14Parser.PseudodestructornameContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#unaryexpression.
  def enterUnaryexpression(self, ctx:CPP14Parser.UnaryexpressionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#unaryexpression.
  def exitUnaryexpression(self, ctx:CPP14Parser.UnaryexpressionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#unaryoperator.
  def enterUnaryoperator(self, ctx:CPP14Parser.UnaryoperatorContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#unaryoperator.
  def exitUnaryoperator(self, ctx:CPP14Parser.UnaryoperatorContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#newexpression.
  def enterNewexpression(self, ctx:CPP14Parser.NewexpressionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#newexpression.
  def exitNewexpression(self, ctx:CPP14Parser.NewexpressionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#newplacement.
  def enterNewplacement(self, ctx:CPP14Parser.NewplacementContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#newplacement.
  def exitNewplacement(self, ctx:CPP14Parser.NewplacementContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#newtypeid.
  def enterNewtypeid(self, ctx:CPP14Parser.NewtypeidContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#newtypeid.
  def exitNewtypeid(self, ctx:CPP14Parser.NewtypeidContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#newdeclarator.
  def enterNewdeclarator(self, ctx:CPP14Parser.NewdeclaratorContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#newdeclarator.
  def exitNewdeclarator(self, ctx:CPP14Parser.NewdeclaratorContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#noptrnewdeclarator.
  def enterNoptrnewdeclarator(self, ctx:CPP14Parser.NoptrnewdeclaratorContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#noptrnewdeclarator.
  def exitNoptrnewdeclarator(self, ctx:CPP14Parser.NoptrnewdeclaratorContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#newinitializer.
  def enterNewinitializer(self, ctx:CPP14Parser.NewinitializerContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#newinitializer.
  def exitNewinitializer(self, ctx:CPP14Parser.NewinitializerContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#deleteexpression.
  def enterDeleteexpression(self, ctx:CPP14Parser.DeleteexpressionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#deleteexpression.
  def exitDeleteexpression(self, ctx:CPP14Parser.DeleteexpressionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#noexceptexpression.
  def enterNoexceptexpression(self, ctx:CPP14Parser.NoexceptexpressionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#noexceptexpression.
  def exitNoexceptexpression(self, ctx:CPP14Parser.NoexceptexpressionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#castexpression.
  def enterCastexpression(self, ctx:CPP14Parser.CastexpressionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#castexpression.
  def exitCastexpression(self, ctx:CPP14Parser.CastexpressionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#pmexpression.
  def enterPmexpression(self, ctx:CPP14Parser.PmexpressionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#pmexpression.
  def exitPmexpression(self, ctx:CPP14Parser.PmexpressionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#multiplicativeexpression.
  def enterMultiplicativeexpression(self, ctx:CPP14Parser.MultiplicativeexpressionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#multiplicativeexpression.
  def exitMultiplicativeexpression(self, ctx:CPP14Parser.MultiplicativeexpressionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#additiveexpression.
  def enterAdditiveexpression(self, ctx:CPP14Parser.AdditiveexpressionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#additiveexpression.
  def exitAdditiveexpression(self, ctx:CPP14Parser.AdditiveexpressionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#shiftexpression.
  def enterShiftexpression(self, ctx:CPP14Parser.ShiftexpressionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#shiftexpression.
  def exitShiftexpression(self, ctx:CPP14Parser.ShiftexpressionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#relationalexpression.
  def enterRelationalexpression(self, ctx:CPP14Parser.RelationalexpressionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#relationalexpression.
  def exitRelationalexpression(self, ctx:CPP14Parser.RelationalexpressionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#equalityexpression.
  def enterEqualityexpression(self, ctx:CPP14Parser.EqualityexpressionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#equalityexpression.
  def exitEqualityexpression(self, ctx:CPP14Parser.EqualityexpressionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#andexpression.
  def enterAndexpression(self, ctx:CPP14Parser.AndexpressionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#andexpression.
  def exitAndexpression(self, ctx:CPP14Parser.AndexpressionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#exclusiveorexpression.
  def enterExclusiveorexpression(self, ctx:CPP14Parser.ExclusiveorexpressionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#exclusiveorexpression.
  def exitExclusiveorexpression(self, ctx:CPP14Parser.ExclusiveorexpressionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#inclusiveorexpression.
  def enterInclusiveorexpression(self, ctx:CPP14Parser.InclusiveorexpressionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#inclusiveorexpression.
  def exitInclusiveorexpression(self, ctx:CPP14Parser.InclusiveorexpressionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#logicalandexpression.
  def enterLogicalandexpression(self, ctx:CPP14Parser.LogicalandexpressionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#logicalandexpression.
  def exitLogicalandexpression(self, ctx:CPP14Parser.LogicalandexpressionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#logicalorexpression.
  def enterLogicalorexpression(self, ctx:CPP14Parser.LogicalorexpressionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#logicalorexpression.
  def exitLogicalorexpression(self, ctx:CPP14Parser.LogicalorexpressionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#conditionalexpression.
  def enterConditionalexpression(self, ctx:CPP14Parser.ConditionalexpressionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#conditionalexpression.
  def exitConditionalexpression(self, ctx:CPP14Parser.ConditionalexpressionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#assignmentexpression.
  def enterAssignmentexpression(self, ctx:CPP14Parser.AssignmentexpressionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#assignmentexpression.
  def exitAssignmentexpression(self, ctx:CPP14Parser.AssignmentexpressionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#assignmentoperator.
  def enterAssignmentoperator(self, ctx:CPP14Parser.AssignmentoperatorContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#assignmentoperator.
  def exitAssignmentoperator(self, ctx:CPP14Parser.AssignmentoperatorContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#expression.
  def enterExpression(self, ctx:CPP14Parser.ExpressionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#expression.
  def exitExpression(self, ctx:CPP14Parser.ExpressionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#constantexpression.
  def enterConstantexpression(self, ctx:CPP14Parser.ConstantexpressionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#constantexpression.
  def exitConstantexpression(self, ctx:CPP14Parser.ConstantexpressionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#statement.
  def enterStatement(self, ctx:CPP14Parser.StatementContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#statement.
  def exitStatement(self, ctx:CPP14Parser.StatementContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#labeledstatement.
  def enterLabeledstatement(self, ctx:CPP14Parser.LabeledstatementContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#labeledstatement.
  def exitLabeledstatement(self, ctx:CPP14Parser.LabeledstatementContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#expressionstatement.
  def enterExpressionstatement(self, ctx:CPP14Parser.ExpressionstatementContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#expressionstatement.
  def exitExpressionstatement(self, ctx:CPP14Parser.ExpressionstatementContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#compoundstatement.
  def enterCompoundstatement(self, ctx:CPP14Parser.CompoundstatementContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#compoundstatement.
  def exitCompoundstatement(self, ctx:CPP14Parser.CompoundstatementContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#statementseq.
  def enterStatementseq(self, ctx:CPP14Parser.StatementseqContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#statementseq.
  def exitStatementseq(self, ctx:CPP14Parser.StatementseqContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#selectionstatement.
  def enterSelectionstatement(self, ctx:CPP14Parser.SelectionstatementContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#selectionstatement.
  def exitSelectionstatement(self, ctx:CPP14Parser.SelectionstatementContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#condition.
  def enterCondition(self, ctx:CPP14Parser.ConditionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#condition.
  def exitCondition(self, ctx:CPP14Parser.ConditionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#iterationstatement.
  def enterIterationstatement(self, ctx:CPP14Parser.IterationstatementContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#iterationstatement.
  def exitIterationstatement(self, ctx:CPP14Parser.IterationstatementContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#forinitstatement.
  def enterForinitstatement(self, ctx:CPP14Parser.ForinitstatementContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#forinitstatement.
  def exitForinitstatement(self, ctx:CPP14Parser.ForinitstatementContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#forrangedeclaration.
  def enterForrangedeclaration(self, ctx:CPP14Parser.ForrangedeclarationContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#forrangedeclaration.
  def exitForrangedeclaration(self, ctx:CPP14Parser.ForrangedeclarationContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#forrangeinitializer.
  def enterForrangeinitializer(self, ctx:CPP14Parser.ForrangeinitializerContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#forrangeinitializer.
  def exitForrangeinitializer(self, ctx:CPP14Parser.ForrangeinitializerContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#jumpstatement.
  def enterJumpstatement(self, ctx:CPP14Parser.JumpstatementContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#jumpstatement.
  def exitJumpstatement(self, ctx:CPP14Parser.JumpstatementContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#declarationstatement.
  def enterDeclarationstatement(self, ctx:CPP14Parser.DeclarationstatementContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#declarationstatement.
  def exitDeclarationstatement(self, ctx:CPP14Parser.DeclarationstatementContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#declarationseq.
  def enterDeclarationseq(self, ctx:CPP14Parser.DeclarationseqContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#declarationseq.
  def exitDeclarationseq(self, ctx:CPP14Parser.DeclarationseqContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#declaration.
  def enterDeclaration(self, ctx:CPP14Parser.DeclarationContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#declaration.
  def exitDeclaration(self, ctx:CPP14Parser.DeclarationContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#blockdeclaration.
  def enterBlockdeclaration(self, ctx:CPP14Parser.BlockdeclarationContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#blockdeclaration.
  def exitBlockdeclaration(self, ctx:CPP14Parser.BlockdeclarationContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#aliasdeclaration.
  def enterAliasdeclaration(self, ctx:CPP14Parser.AliasdeclarationContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#aliasdeclaration.
  def exitAliasdeclaration(self, ctx:CPP14Parser.AliasdeclarationContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#simpledeclaration.
  def enterSimpledeclaration(self, ctx:CPP14Parser.SimpledeclarationContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#simpledeclaration.
  def exitSimpledeclaration(self, ctx:CPP14Parser.SimpledeclarationContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#static_assertdeclaration.
  def enterStatic_assertdeclaration(self, ctx:CPP14Parser.Static_assertdeclarationContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#static_assertdeclaration.
  def exitStatic_assertdeclaration(self, ctx:CPP14Parser.Static_assertdeclarationContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#emptydeclaration.
  def enterEmptydeclaration(self, ctx:CPP14Parser.EmptydeclarationContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#emptydeclaration.
  def exitEmptydeclaration(self, ctx:CPP14Parser.EmptydeclarationContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#attributedeclaration.
  def enterAttributedeclaration(self, ctx:CPP14Parser.AttributedeclarationContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#attributedeclaration.
  def exitAttributedeclaration(self, ctx:CPP14Parser.AttributedeclarationContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#declspecifier.
  def enterDeclspecifier(self, ctx:CPP14Parser.DeclspecifierContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#declspecifier.
  def exitDeclspecifier(self, ctx:CPP14Parser.DeclspecifierContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#declspecifierseq.
  def enterDeclspecifierseq(self, ctx:CPP14Parser.DeclspecifierseqContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#declspecifierseq.
  def exitDeclspecifierseq(self, ctx:CPP14Parser.DeclspecifierseqContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#storageclassspecifier.
  def enterStorageclassspecifier(self, ctx:CPP14Parser.StorageclassspecifierContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#storageclassspecifier.
  def exitStorageclassspecifier(self, ctx:CPP14Parser.StorageclassspecifierContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#functionspecifier.
  def enterFunctionspecifier(self, ctx:CPP14Parser.FunctionspecifierContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#functionspecifier.
  def exitFunctionspecifier(self, ctx:CPP14Parser.FunctionspecifierContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#typedefname.
  def enterTypedefname(self, ctx:CPP14Parser.TypedefnameContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#typedefname.
  def exitTypedefname(self, ctx:CPP14Parser.TypedefnameContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#typespecifier.
  def enterTypespecifier(self, ctx:CPP14Parser.TypespecifierContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#typespecifier.
  def exitTypespecifier(self, ctx:CPP14Parser.TypespecifierContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#trailingtypespecifier.
  def enterTrailingtypespecifier(self, ctx:CPP14Parser.TrailingtypespecifierContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#trailingtypespecifier.
  def exitTrailingtypespecifier(self, ctx:CPP14Parser.TrailingtypespecifierContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#typespecifierseq.
  def enterTypespecifierseq(self, ctx:CPP14Parser.TypespecifierseqContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#typespecifierseq.
  def exitTypespecifierseq(self, ctx:CPP14Parser.TypespecifierseqContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#trailingtypespecifierseq.
  def enterTrailingtypespecifierseq(self, ctx:CPP14Parser.TrailingtypespecifierseqContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#trailingtypespecifierseq.
  def exitTrailingtypespecifierseq(self, ctx:CPP14Parser.TrailingtypespecifierseqContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#simpletypespecifier.
  def enterSimpletypespecifier(self, ctx:CPP14Parser.SimpletypespecifierContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#simpletypespecifier.
  def exitSimpletypespecifier(self, ctx:CPP14Parser.SimpletypespecifierContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#thetypename.
  def enterThetypename(self, ctx:CPP14Parser.ThetypenameContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#thetypename.
  def exitThetypename(self, ctx:CPP14Parser.ThetypenameContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#decltypespecifier.
  def enterDecltypespecifier(self, ctx:CPP14Parser.DecltypespecifierContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#decltypespecifier.
  def exitDecltypespecifier(self, ctx:CPP14Parser.DecltypespecifierContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#elaboratedtypespecifier.
  def enterElaboratedtypespecifier(self, ctx:CPP14Parser.ElaboratedtypespecifierContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#elaboratedtypespecifier.
  def exitElaboratedtypespecifier(self, ctx:CPP14Parser.ElaboratedtypespecifierContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#enumname.
  def enterEnumname(self, ctx:CPP14Parser.EnumnameContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#enumname.
  def exitEnumname(self, ctx:CPP14Parser.EnumnameContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#enumspecifier.
  def enterEnumspecifier(self, ctx:CPP14Parser.EnumspecifierContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#enumspecifier.
  def exitEnumspecifier(self, ctx:CPP14Parser.EnumspecifierContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#enumhead.
  def enterEnumhead(self, ctx:CPP14Parser.EnumheadContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#enumhead.
  def exitEnumhead(self, ctx:CPP14Parser.EnumheadContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#opaqueenumdeclaration.
  def enterOpaqueenumdeclaration(self, ctx:CPP14Parser.OpaqueenumdeclarationContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#opaqueenumdeclaration.
  def exitOpaqueenumdeclaration(self, ctx:CPP14Parser.OpaqueenumdeclarationContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#enumkey.
  def enterEnumkey(self, ctx:CPP14Parser.EnumkeyContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#enumkey.
  def exitEnumkey(self, ctx:CPP14Parser.EnumkeyContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#enumbase.
  def enterEnumbase(self, ctx:CPP14Parser.EnumbaseContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#enumbase.
  def exitEnumbase(self, ctx:CPP14Parser.EnumbaseContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#enumeratorlist.
  def enterEnumeratorlist(self, ctx:CPP14Parser.EnumeratorlistContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#enumeratorlist.
  def exitEnumeratorlist(self, ctx:CPP14Parser.EnumeratorlistContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#enumeratordefinition.
  def enterEnumeratordefinition(self, ctx:CPP14Parser.EnumeratordefinitionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#enumeratordefinition.
  def exitEnumeratordefinition(self, ctx:CPP14Parser.EnumeratordefinitionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#enumerator.
  def enterEnumerator(self, ctx:CPP14Parser.EnumeratorContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#enumerator.
  def exitEnumerator(self, ctx:CPP14Parser.EnumeratorContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#namespacename.
  def enterNamespacename(self, ctx:CPP14Parser.NamespacenameContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#namespacename.
  def exitNamespacename(self, ctx:CPP14Parser.NamespacenameContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#originalnamespacename.
  def enterOriginalnamespacename(self, ctx:CPP14Parser.OriginalnamespacenameContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#originalnamespacename.
  def exitOriginalnamespacename(self, ctx:CPP14Parser.OriginalnamespacenameContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#namespacedefinition.
  def enterNamespacedefinition(self, ctx:CPP14Parser.NamespacedefinitionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#namespacedefinition.
  def exitNamespacedefinition(self, ctx:CPP14Parser.NamespacedefinitionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#namednamespacedefinition.
  def enterNamednamespacedefinition(self, ctx:CPP14Parser.NamednamespacedefinitionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#namednamespacedefinition.
  def exitNamednamespacedefinition(self, ctx:CPP14Parser.NamednamespacedefinitionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#originalnamespacedefinition.
  def enterOriginalnamespacedefinition(self, ctx:CPP14Parser.OriginalnamespacedefinitionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#originalnamespacedefinition.
  def exitOriginalnamespacedefinition(self, ctx:CPP14Parser.OriginalnamespacedefinitionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#extensionnamespacedefinition.
  def enterExtensionnamespacedefinition(self, ctx:CPP14Parser.ExtensionnamespacedefinitionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#extensionnamespacedefinition.
  def exitExtensionnamespacedefinition(self, ctx:CPP14Parser.ExtensionnamespacedefinitionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#unnamednamespacedefinition.
  def enterUnnamednamespacedefinition(self, ctx:CPP14Parser.UnnamednamespacedefinitionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#unnamednamespacedefinition.
  def exitUnnamednamespacedefinition(self, ctx:CPP14Parser.UnnamednamespacedefinitionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#namespacebody.
  def enterNamespacebody(self, ctx:CPP14Parser.NamespacebodyContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#namespacebody.
  def exitNamespacebody(self, ctx:CPP14Parser.NamespacebodyContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#namespacealias.
  def enterNamespacealias(self, ctx:CPP14Parser.NamespacealiasContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#namespacealias.
  def exitNamespacealias(self, ctx:CPP14Parser.NamespacealiasContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#namespacealiasdefinition.
  def enterNamespacealiasdefinition(self, ctx:CPP14Parser.NamespacealiasdefinitionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#namespacealiasdefinition.
  def exitNamespacealiasdefinition(self, ctx:CPP14Parser.NamespacealiasdefinitionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#qualifiednamespacespecifier.
  def enterQualifiednamespacespecifier(self, ctx:CPP14Parser.QualifiednamespacespecifierContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#qualifiednamespacespecifier.
  def exitQualifiednamespacespecifier(self, ctx:CPP14Parser.QualifiednamespacespecifierContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#usingdeclaration.
  def enterUsingdeclaration(self, ctx:CPP14Parser.UsingdeclarationContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#usingdeclaration.
  def exitUsingdeclaration(self, ctx:CPP14Parser.UsingdeclarationContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#usingdirective.
  def enterUsingdirective(self, ctx:CPP14Parser.UsingdirectiveContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#usingdirective.
  def exitUsingdirective(self, ctx:CPP14Parser.UsingdirectiveContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#asmdefinition.
  def enterAsmdefinition(self, ctx:CPP14Parser.AsmdefinitionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#asmdefinition.
  def exitAsmdefinition(self, ctx:CPP14Parser.AsmdefinitionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#linkagespecification.
  def enterLinkagespecification(self, ctx:CPP14Parser.LinkagespecificationContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#linkagespecification.
  def exitLinkagespecification(self, ctx:CPP14Parser.LinkagespecificationContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#attributespecifierseq.
  def enterAttributespecifierseq(self, ctx:CPP14Parser.AttributespecifierseqContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#attributespecifierseq.
  def exitAttributespecifierseq(self, ctx:CPP14Parser.AttributespecifierseqContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#attributespecifier.
  def enterAttributespecifier(self, ctx:CPP14Parser.AttributespecifierContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#attributespecifier.
  def exitAttributespecifier(self, ctx:CPP14Parser.AttributespecifierContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#alignmentspecifier.
  def enterAlignmentspecifier(self, ctx:CPP14Parser.AlignmentspecifierContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#alignmentspecifier.
  def exitAlignmentspecifier(self, ctx:CPP14Parser.AlignmentspecifierContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#attributelist.
  def enterAttributelist(self, ctx:CPP14Parser.AttributelistContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#attributelist.
  def exitAttributelist(self, ctx:CPP14Parser.AttributelistContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#attribute.
  def enterAttribute(self, ctx:CPP14Parser.AttributeContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#attribute.
  def exitAttribute(self, ctx:CPP14Parser.AttributeContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#attributetoken.
  def enterAttributetoken(self, ctx:CPP14Parser.AttributetokenContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#attributetoken.
  def exitAttributetoken(self, ctx:CPP14Parser.AttributetokenContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#attributescopedtoken.
  def enterAttributescopedtoken(self, ctx:CPP14Parser.AttributescopedtokenContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#attributescopedtoken.
  def exitAttributescopedtoken(self, ctx:CPP14Parser.AttributescopedtokenContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#attributenamespace.
  def enterAttributenamespace(self, ctx:CPP14Parser.AttributenamespaceContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#attributenamespace.
  def exitAttributenamespace(self, ctx:CPP14Parser.AttributenamespaceContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#attributeargumentclause.
  def enterAttributeargumentclause(self, ctx:CPP14Parser.AttributeargumentclauseContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#attributeargumentclause.
  def exitAttributeargumentclause(self, ctx:CPP14Parser.AttributeargumentclauseContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#balancedtokenseq.
  def enterBalancedtokenseq(self, ctx:CPP14Parser.BalancedtokenseqContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#balancedtokenseq.
  def exitBalancedtokenseq(self, ctx:CPP14Parser.BalancedtokenseqContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#balancedtoken.
  def enterBalancedtoken(self, ctx:CPP14Parser.BalancedtokenContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#balancedtoken.
  def exitBalancedtoken(self, ctx:CPP14Parser.BalancedtokenContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#initdeclaratorlist.
  def enterInitdeclaratorlist(self, ctx:CPP14Parser.InitdeclaratorlistContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#initdeclaratorlist.
  def exitInitdeclaratorlist(self, ctx:CPP14Parser.InitdeclaratorlistContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#initdeclarator.
  def enterInitdeclarator(self, ctx:CPP14Parser.InitdeclaratorContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#initdeclarator.
  def exitInitdeclarator(self, ctx:CPP14Parser.InitdeclaratorContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#declarator.
  def enterDeclarator(self, ctx:CPP14Parser.DeclaratorContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#declarator.
  def exitDeclarator(self, ctx:CPP14Parser.DeclaratorContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#ptrdeclarator.
  def enterPtrdeclarator(self, ctx:CPP14Parser.PtrdeclaratorContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#ptrdeclarator.
  def exitPtrdeclarator(self, ctx:CPP14Parser.PtrdeclaratorContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#noptrdeclarator.
  def enterNoptrdeclarator(self, ctx:CPP14Parser.NoptrdeclaratorContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#noptrdeclarator.
  def exitNoptrdeclarator(self, ctx:CPP14Parser.NoptrdeclaratorContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#parametersandqualifiers.
  def enterParametersandqualifiers(self, ctx:CPP14Parser.ParametersandqualifiersContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#parametersandqualifiers.
  def exitParametersandqualifiers(self, ctx:CPP14Parser.ParametersandqualifiersContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#trailingreturntype.
  def enterTrailingreturntype(self, ctx:CPP14Parser.TrailingreturntypeContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#trailingreturntype.
  def exitTrailingreturntype(self, ctx:CPP14Parser.TrailingreturntypeContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#ptroperator.
  def enterPtroperator(self, ctx:CPP14Parser.PtroperatorContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#ptroperator.
  def exitPtroperator(self, ctx:CPP14Parser.PtroperatorContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#cvqualifierseq.
  def enterCvqualifierseq(self, ctx:CPP14Parser.CvqualifierseqContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#cvqualifierseq.
  def exitCvqualifierseq(self, ctx:CPP14Parser.CvqualifierseqContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#cvqualifier.
  def enterCvqualifier(self, ctx:CPP14Parser.CvqualifierContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#cvqualifier.
  def exitCvqualifier(self, ctx:CPP14Parser.CvqualifierContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#refqualifier.
  def enterRefqualifier(self, ctx:CPP14Parser.RefqualifierContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#refqualifier.
  def exitRefqualifier(self, ctx:CPP14Parser.RefqualifierContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#declaratorid.
  def enterDeclaratorid(self, ctx:CPP14Parser.DeclaratoridContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#declaratorid.
  def exitDeclaratorid(self, ctx:CPP14Parser.DeclaratoridContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#thetypeid.
  def enterThetypeid(self, ctx:CPP14Parser.ThetypeidContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#thetypeid.
  def exitThetypeid(self, ctx:CPP14Parser.ThetypeidContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#abstractdeclarator.
  def enterAbstractdeclarator(self, ctx:CPP14Parser.AbstractdeclaratorContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#abstractdeclarator.
  def exitAbstractdeclarator(self, ctx:CPP14Parser.AbstractdeclaratorContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#ptrabstractdeclarator.
  def enterPtrabstractdeclarator(self, ctx:CPP14Parser.PtrabstractdeclaratorContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#ptrabstractdeclarator.
  def exitPtrabstractdeclarator(self, ctx:CPP14Parser.PtrabstractdeclaratorContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#noptrabstractdeclarator.
  def enterNoptrabstractdeclarator(self, ctx:CPP14Parser.NoptrabstractdeclaratorContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#noptrabstractdeclarator.
  def exitNoptrabstractdeclarator(self, ctx:CPP14Parser.NoptrabstractdeclaratorContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#abstractpackdeclarator.
  def enterAbstractpackdeclarator(self, ctx:CPP14Parser.AbstractpackdeclaratorContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#abstractpackdeclarator.
  def exitAbstractpackdeclarator(self, ctx:CPP14Parser.AbstractpackdeclaratorContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#noptrabstractpackdeclarator.
  def enterNoptrabstractpackdeclarator(self, ctx:CPP14Parser.NoptrabstractpackdeclaratorContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#noptrabstractpackdeclarator.
  def exitNoptrabstractpackdeclarator(self, ctx:CPP14Parser.NoptrabstractpackdeclaratorContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#parameterdeclarationclause.
  def enterParameterdeclarationclause(self, ctx:CPP14Parser.ParameterdeclarationclauseContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#parameterdeclarationclause.
  def exitParameterdeclarationclause(self, ctx:CPP14Parser.ParameterdeclarationclauseContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#parameterdeclarationlist.
  def enterParameterdeclarationlist(self, ctx:CPP14Parser.ParameterdeclarationlistContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#parameterdeclarationlist.
  def exitParameterdeclarationlist(self, ctx:CPP14Parser.ParameterdeclarationlistContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#parameterdeclaration.
  def enterParameterdeclaration(self, ctx:CPP14Parser.ParameterdeclarationContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#parameterdeclaration.
  def exitParameterdeclaration(self, ctx:CPP14Parser.ParameterdeclarationContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#functiondefinition.
  def enterFunctiondefinition(self, ctx:CPP14Parser.FunctiondefinitionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#functiondefinition.
  def exitFunctiondefinition(self, ctx:CPP14Parser.FunctiondefinitionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#functionbody.
  def enterFunctionbody(self, ctx:CPP14Parser.FunctionbodyContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#functionbody.
  def exitFunctionbody(self, ctx:CPP14Parser.FunctionbodyContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#initializer.
  def enterInitializer(self, ctx:CPP14Parser.InitializerContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#initializer.
  def exitInitializer(self, ctx:CPP14Parser.InitializerContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#braceorequalinitializer.
  def enterBraceorequalinitializer(self, ctx:CPP14Parser.BraceorequalinitializerContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#braceorequalinitializer.
  def exitBraceorequalinitializer(self, ctx:CPP14Parser.BraceorequalinitializerContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#initializerclause.
  def enterInitializerclause(self, ctx:CPP14Parser.InitializerclauseContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#initializerclause.
  def exitInitializerclause(self, ctx:CPP14Parser.InitializerclauseContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#initializerlist.
  def enterInitializerlist(self, ctx:CPP14Parser.InitializerlistContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#initializerlist.
  def exitInitializerlist(self, ctx:CPP14Parser.InitializerlistContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#bracedinitlist.
  def enterBracedinitlist(self, ctx:CPP14Parser.BracedinitlistContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#bracedinitlist.
  def exitBracedinitlist(self, ctx:CPP14Parser.BracedinitlistContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#classname.
  def enterClassname(self, ctx:CPP14Parser.ClassnameContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#classname.
  def exitClassname(self, ctx:CPP14Parser.ClassnameContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#classspecifier.
  def enterClassspecifier(self, ctx:CPP14Parser.ClassspecifierContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#classspecifier.
  def exitClassspecifier(self, ctx:CPP14Parser.ClassspecifierContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#classhead.
  def enterClasshead(self, ctx:CPP14Parser.ClassheadContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#classhead.
  def exitClasshead(self, ctx:CPP14Parser.ClassheadContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#classheadname.
  def enterClassheadname(self, ctx:CPP14Parser.ClassheadnameContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#classheadname.
  def exitClassheadname(self, ctx:CPP14Parser.ClassheadnameContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#classvirtspecifier.
  def enterClassvirtspecifier(self, ctx:CPP14Parser.ClassvirtspecifierContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#classvirtspecifier.
  def exitClassvirtspecifier(self, ctx:CPP14Parser.ClassvirtspecifierContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#classkey.
  def enterClasskey(self, ctx:CPP14Parser.ClasskeyContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#classkey.
  def exitClasskey(self, ctx:CPP14Parser.ClasskeyContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#memberspecification.
  def enterMemberspecification(self, ctx:CPP14Parser.MemberspecificationContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#memberspecification.
  def exitMemberspecification(self, ctx:CPP14Parser.MemberspecificationContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#memberdeclaration.
  def enterMemberdeclaration(self, ctx:CPP14Parser.MemberdeclarationContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#memberdeclaration.
  def exitMemberdeclaration(self, ctx:CPP14Parser.MemberdeclarationContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#memberdeclaratorlist.
  def enterMemberdeclaratorlist(self, ctx:CPP14Parser.MemberdeclaratorlistContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#memberdeclaratorlist.
  def exitMemberdeclaratorlist(self, ctx:CPP14Parser.MemberdeclaratorlistContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#memberdeclarator.
  def enterMemberdeclarator(self, ctx:CPP14Parser.MemberdeclaratorContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#memberdeclarator.
  def exitMemberdeclarator(self, ctx:CPP14Parser.MemberdeclaratorContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#virtspecifierseq.
  def enterVirtspecifierseq(self, ctx:CPP14Parser.VirtspecifierseqContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#virtspecifierseq.
  def exitVirtspecifierseq(self, ctx:CPP14Parser.VirtspecifierseqContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#virtspecifier.
  def enterVirtspecifier(self, ctx:CPP14Parser.VirtspecifierContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#virtspecifier.
  def exitVirtspecifier(self, ctx:CPP14Parser.VirtspecifierContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#purespecifier.
  def enterPurespecifier(self, ctx:CPP14Parser.PurespecifierContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#purespecifier.
  def exitPurespecifier(self, ctx:CPP14Parser.PurespecifierContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#baseclause.
  def enterBaseclause(self, ctx:CPP14Parser.BaseclauseContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#baseclause.
  def exitBaseclause(self, ctx:CPP14Parser.BaseclauseContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#basespecifierlist.
  def enterBasespecifierlist(self, ctx:CPP14Parser.BasespecifierlistContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#basespecifierlist.
  def exitBasespecifierlist(self, ctx:CPP14Parser.BasespecifierlistContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#basespecifier.
  def enterBasespecifier(self, ctx:CPP14Parser.BasespecifierContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#basespecifier.
  def exitBasespecifier(self, ctx:CPP14Parser.BasespecifierContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#classordecltype.
  def enterClassordecltype(self, ctx:CPP14Parser.ClassordecltypeContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#classordecltype.
  def exitClassordecltype(self, ctx:CPP14Parser.ClassordecltypeContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#basetypespecifier.
  def enterBasetypespecifier(self, ctx:CPP14Parser.BasetypespecifierContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#basetypespecifier.
  def exitBasetypespecifier(self, ctx:CPP14Parser.BasetypespecifierContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#accessspecifier.
  def enterAccessspecifier(self, ctx:CPP14Parser.AccessspecifierContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#accessspecifier.
  def exitAccessspecifier(self, ctx:CPP14Parser.AccessspecifierContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#conversionfunctionid.
  def enterConversionfunctionid(self, ctx:CPP14Parser.ConversionfunctionidContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#conversionfunctionid.
  def exitConversionfunctionid(self, ctx:CPP14Parser.ConversionfunctionidContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#conversiontypeid.
  def enterConversiontypeid(self, ctx:CPP14Parser.ConversiontypeidContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#conversiontypeid.
  def exitConversiontypeid(self, ctx:CPP14Parser.ConversiontypeidContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#conversiondeclarator.
  def enterConversiondeclarator(self, ctx:CPP14Parser.ConversiondeclaratorContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#conversiondeclarator.
  def exitConversiondeclarator(self, ctx:CPP14Parser.ConversiondeclaratorContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#ctorinitializer.
  def enterCtorinitializer(self, ctx:CPP14Parser.CtorinitializerContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#ctorinitializer.
  def exitCtorinitializer(self, ctx:CPP14Parser.CtorinitializerContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#meminitializerlist.
  def enterMeminitializerlist(self, ctx:CPP14Parser.MeminitializerlistContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#meminitializerlist.
  def exitMeminitializerlist(self, ctx:CPP14Parser.MeminitializerlistContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#meminitializer.
  def enterMeminitializer(self, ctx:CPP14Parser.MeminitializerContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#meminitializer.
  def exitMeminitializer(self, ctx:CPP14Parser.MeminitializerContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#meminitializerid.
  def enterMeminitializerid(self, ctx:CPP14Parser.MeminitializeridContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#meminitializerid.
  def exitMeminitializerid(self, ctx:CPP14Parser.MeminitializeridContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#operatorfunctionid.
  def enterOperatorfunctionid(self, ctx:CPP14Parser.OperatorfunctionidContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#operatorfunctionid.
  def exitOperatorfunctionid(self, ctx:CPP14Parser.OperatorfunctionidContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#literaloperatorid.
  def enterLiteraloperatorid(self, ctx:CPP14Parser.LiteraloperatoridContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#literaloperatorid.
  def exitLiteraloperatorid(self, ctx:CPP14Parser.LiteraloperatoridContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#templatedeclaration.
  def enterTemplatedeclaration(self, ctx:CPP14Parser.TemplatedeclarationContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#templatedeclaration.
  def exitTemplatedeclaration(self, ctx:CPP14Parser.TemplatedeclarationContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#templateparameterlist.
  def enterTemplateparameterlist(self, ctx:CPP14Parser.TemplateparameterlistContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#templateparameterlist.
  def exitTemplateparameterlist(self, ctx:CPP14Parser.TemplateparameterlistContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#templateparameter.
  def enterTemplateparameter(self, ctx:CPP14Parser.TemplateparameterContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#templateparameter.
  def exitTemplateparameter(self, ctx:CPP14Parser.TemplateparameterContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#typeparameter.
  def enterTypeparameter(self, ctx:CPP14Parser.TypeparameterContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#typeparameter.
  def exitTypeparameter(self, ctx:CPP14Parser.TypeparameterContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#simpletemplateid.
  def enterSimpletemplateid(self, ctx:CPP14Parser.SimpletemplateidContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#simpletemplateid.
  def exitSimpletemplateid(self, ctx:CPP14Parser.SimpletemplateidContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#templateid.
  def enterTemplateid(self, ctx:CPP14Parser.TemplateidContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#templateid.
  def exitTemplateid(self, ctx:CPP14Parser.TemplateidContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#templatename.
  def enterTemplatename(self, ctx:CPP14Parser.TemplatenameContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#templatename.
  def exitTemplatename(self, ctx:CPP14Parser.TemplatenameContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#templateargumentlist.
  def enterTemplateargumentlist(self, ctx:CPP14Parser.TemplateargumentlistContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#templateargumentlist.
  def exitTemplateargumentlist(self, ctx:CPP14Parser.TemplateargumentlistContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#templateargument.
  def enterTemplateargument(self, ctx:CPP14Parser.TemplateargumentContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#templateargument.
  def exitTemplateargument(self, ctx:CPP14Parser.TemplateargumentContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#typenamespecifier.
  def enterTypenamespecifier(self, ctx:CPP14Parser.TypenamespecifierContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#typenamespecifier.
  def exitTypenamespecifier(self, ctx:CPP14Parser.TypenamespecifierContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#explicitinstantiation.
  def enterExplicitinstantiation(self, ctx:CPP14Parser.ExplicitinstantiationContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#explicitinstantiation.
  def exitExplicitinstantiation(self, ctx:CPP14Parser.ExplicitinstantiationContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#explicitspecialization.
  def enterExplicitspecialization(self, ctx:CPP14Parser.ExplicitspecializationContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#explicitspecialization.
  def exitExplicitspecialization(self, ctx:CPP14Parser.ExplicitspecializationContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#tryblock.
  def enterTryblock(self, ctx:CPP14Parser.TryblockContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#tryblock.
  def exitTryblock(self, ctx:CPP14Parser.TryblockContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#functiontryblock.
  def enterFunctiontryblock(self, ctx:CPP14Parser.FunctiontryblockContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#functiontryblock.
  def exitFunctiontryblock(self, ctx:CPP14Parser.FunctiontryblockContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#handlerseq.
  def enterHandlerseq(self, ctx:CPP14Parser.HandlerseqContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#handlerseq.
  def exitHandlerseq(self, ctx:CPP14Parser.HandlerseqContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#handler.
  def enterHandler(self, ctx:CPP14Parser.HandlerContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#handler.
  def exitHandler(self, ctx:CPP14Parser.HandlerContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#exceptiondeclaration.
  def enterExceptiondeclaration(self, ctx:CPP14Parser.ExceptiondeclarationContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#exceptiondeclaration.
  def exitExceptiondeclaration(self, ctx:CPP14Parser.ExceptiondeclarationContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#throwexpression.
  def enterThrowexpression(self, ctx:CPP14Parser.ThrowexpressionContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#throwexpression.
  def exitThrowexpression(self, ctx:CPP14Parser.ThrowexpressionContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#exceptionspecification.
  def enterExceptionspecification(self, ctx:CPP14Parser.ExceptionspecificationContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#exceptionspecification.
  def exitExceptionspecification(self, ctx:CPP14Parser.ExceptionspecificationContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#dynamicexceptionspecification.
  def enterDynamicexceptionspecification(self, ctx:CPP14Parser.DynamicexceptionspecificationContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#dynamicexceptionspecification.
  def exitDynamicexceptionspecification(self, ctx:CPP14Parser.DynamicexceptionspecificationContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#typeidlist.
  def enterTypeidlist(self, ctx:CPP14Parser.TypeidlistContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#typeidlist.
  def exitTypeidlist(self, ctx:CPP14Parser.TypeidlistContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#noexceptspecification.
  def enterNoexceptspecification(self, ctx:CPP14Parser.NoexceptspecificationContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#noexceptspecification.
  def exitNoexceptspecification(self, ctx:CPP14Parser.NoexceptspecificationContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#rightShift.
  def enterRightShift(self, ctx:CPP14Parser.RightShiftContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#rightShift.
  def exitRightShift(self, ctx:CPP14Parser.RightShiftContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#rightShiftAssign.
  def enterRightShiftAssign(self, ctx:CPP14Parser.RightShiftAssignContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#rightShiftAssign.
  def exitRightShiftAssign(self, ctx:CPP14Parser.RightShiftAssignContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#theoperator.
  def enterTheoperator(self, ctx:CPP14Parser.TheoperatorContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#theoperator.
  def exitTheoperator(self, ctx:CPP14Parser.TheoperatorContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#literal.
  def enterLiteral(self, ctx:CPP14Parser.LiteralContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#literal.
  def exitLiteral(self, ctx:CPP14Parser.LiteralContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#booleanliteral.
  def enterBooleanliteral(self, ctx:CPP14Parser.BooleanliteralContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#booleanliteral.
  def exitBooleanliteral(self, ctx:CPP14Parser.BooleanliteralContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#pointerliteral.
  def enterPointerliteral(self, ctx:CPP14Parser.PointerliteralContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#pointerliteral.
  def exitPointerliteral(self, ctx:CPP14Parser.PointerliteralContext):
    self.ls.append(ctx)


  # Enter a parse tree produced by CPP14Parser#userdefinedliteral.
  def enterUserdefinedliteral(self, ctx:CPP14Parser.UserdefinedliteralContext):
    self.ls.append(ctx)

  # Exit a parse tree produced by CPP14Parser#userdefinedliteral.
  def exitUserdefinedliteral(self, ctx:CPP14Parser.UserdefinedliteralContext):
    self.ls.append(ctx)


