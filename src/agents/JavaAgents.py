import sys
import re
import logging
import antlr4
import subprocess

from antlr.JavaParser import JavaParser

from agents.JavaAgentBase import GetIsJavaMcFn, JavaAgentBase, JavaRefactorAgent

def _AddDefaultArguments(parser, keyword):
  temp_group = parser.add_mutually_exclusive_group()
  temp_group.add_argument(
      '--method-declaration',
      help='Specify the method declarition name, e.g. `--method-declaration '
           'func would %s inside the statments inside func declaration'
           % keyword)
  temp_group.add_argument(
      '--method-invocation',
      help='Specify the method invocation name, e.g. `--method-invocation'
           ' func would %s before each call'
           % keyword)
  group = parser.add_mutually_exclusive_group()
  group.add_argument(
      '--%s-each-line' % keyword, action='store_true', default=False,
      help='Add %s in between each statement' % keyword)
  group.add_argument(
      '--%s-entry-exit' % keyword, action='store_true', default=False,
      help='Add %s only at block entry and exit' % keyword)
  return parser


class AndroidJavaLogAgent(JavaRefactorAgent):
  """Add Logging to Java Method or Classes"""
  @staticmethod
  def addOptions(parser):
    parser = _AddDefaultArguments(parser, 'log')
    #TODO add support for the commented out arguments
#     parser.add_argument('--log-method-local-variable', action='store_true',
        # default=False, help='Log all the local variable declared in a specified'
                            # ' method')
    # parser.add_argument('--log-class-variable', action='store_true',
        # default=False, help='Log all the class variables at each command line')
    parser.add_argument('--log-variable', help='Log the specified variable at '
                        'each line. e.g. `--log-variable=mFlag` would cause'
                        ' mFlag to be logged each time')
    parser.add_argument(
        '--log-format', choices=['counter', 'line', 'source'], default='line',
        help='Use number counting in log content')
    parser.add_argument(
        '--tag', default='#SAUL', help='Specify the tag used for logging')
    parser.add_argument(
        '--call', default='d', choices=['d', 'i', 'w', 'e'],
        help='Specify which log method to use [d, i, w, e]. `d` is default')
    parser.add_argument(
        '--package', default='android.util.Log',
        help='Specify which logging package to use')
    parser.add_argument(
        '--byol', '--bring-your-own-log', dest='bring_your_own_log',
        help='Specify your own log statement, e.g. '
             '--bring-your-own-log=Log.d("#SAUL", Integer.toString(mInt))')
    return parser

  def __init__(self, args):
    super(AndroidJavaLogAgent, self).__init__(args)
    self.log_content = None
    self.log_formatter = None
    self.counter = 0

  #Override
  def validate(self):
    pass

  #Override
  def actions(self):
    log_template = self.getLogTemplate()
    self.addImport(self.args.package)
    if self.args.method_declaration:
      self.refactor.actionOnX(
          self.tb, JavaParser.ConstructorDeclarationContext,
          condition_fn = (
            lambda x: x.IDENTIFIER().getText() == self.args.method_declaration),
          action_fn = self._getLogEveryStatementFn(log_template))
      self.refactor.actionOnX(
          self.tb, JavaParser.MethodDeclarationContext,
          condition_fn = (
            lambda x: x.IDENTIFIER().getText() == self.args.method_declaration),
          action_fn = self._getLogEveryStatementFn(log_template))
    elif self.args.method_invocation:
      self.refactor.actionOnX(
          self.tb, JavaParser.StatementContext,
          condition_fn = GetIsJavaMcFn(self.args.method_invocation),
          action_fn = self.refactor.getInsertBeforeTokenFn(
              log_template, use_mask=True))
    else:
      self.refactor.actionOnX(
          self.tb, JavaParser.MethodDeclarationContext,
          action_fn = self._getLogEveryStatementFn(log_template))
      self.refactor.actionOnX(
          self.tb, JavaParser.ConstructorDeclarationContext,
          action_fn = self._getLogEveryStatementFn(log_template))

    self.refactor.save()

  def _counterLogFormatter(self, template, _):
    self.counter += 1
    return template.format(class_name=self.class_name, counter=self.counter)

  def _lineNumLogFormatter(self, template, token):
    line_num = (
        str(token.start.line) if token.start.line == token.stop.line else
        '%d-%d' % (token.start.line, token.stop.line))
    return template.format(class_name=self.class_name, line_num=line_num)

  def _sourceLogFormatter(self, template, token):
    line_num = (
        str(token.start.line) if token.start.line == token.stop.line else
        '%d-%d' % (token.start.line, token.stop.line))
    code = (
        ' ' * token.depth()
        + self.refactor.content[token.start.start:token.stop.stop+1])
    code = code.split('\n')[0]
    code = code.replace('"', r'\"')
    return template.format(
      class_name=self.class_name, line_num=line_num, code=code)

  def getLogTemplate(self):
    if self.args.bring_your_own_log:
      self.log_content = self.args.bring_your_own_log
      self.log_formatter = lambda tem, _: tem
    if self.args.log_format == 'counter':
      self.log_content = "{class_name}:{counter:d}"
      self.log_formatter = self._counterLogFormatter
    elif self.args.log_format == 'line':
      self.log_content = "{class_name}:{line_num}"
      self.log_formatter = self._lineNumLogFormatter
    elif self.args.log_format == 'source':
      self.log_content = "{class_name}:{line_num} {code}"
      self.log_formatter = self._sourceLogFormatter
    # default choice
    else:
      self.log_content = "{class_name}:{line_num}"
      self.log_formatter = self._lineNumLogFormatter
    return 'Log.%s("%s", "%s");' % (
        self.args.call, self.args.tag, self.log_content)

  def _logEveryStatement(self, token, log_template):
    if type(token) == antlr4.tree.Tree.TerminalNodeImpl:
      return
    for c in token.getChildren():
      if type(c) == JavaParser.BlockStatementContext:
        log_insertion = self.log_formatter(log_template, c)
        self.refactor.insertBeforeToken(c, log_insertion, use_mask=True)
      self._logEveryStatement(c, log_template)

  def _getLogEveryStatementFn(self, log_template):
    def _inner_function(token):
      self._logEveryStatement(token, log_template)
    return _inner_function

class AndroidJavaTraceAgent(JavaRefactorAgent):
  """Add Tracing to Java Method or Classes"""
  @staticmethod
  def addOptions(parser):
    parser = _AddDefaultArguments(parser, 'trace')
    parser.add_argument(
        '--package', default='org.chromium.base.test.TestTraceEvent',
        help='Specify which logging package to use')
    return parser

  def __init__(self, args):
    super(AndroidJavaTraceAgent, self).__init__(args)
    self.trace_content = None
    self.trace_formatter = None

  #Override
  def validate(self):
    pass

  #Override
  def actions(self):
    trace_template = self.getTraceTemplate()
    self.addImport(self.args.package)
    self.refactor.actionOnX(
        self.tb, JavaParser.MethodDeclarationContext,
        action_fn = self._getTraceEveryStatementFn(trace_template))
    self.refactor.save()

  def _lineNumLogFormatter(self, template, token, call):
    line_num = (
        str(token.start.line) if token.start.line == token.stop.line else
        '%d-%d' % (token.start.line, token.stop.line))
    return template.format(
        call=call, class_name=self.class_name, line_num=line_num)

  def getTraceTemplate(self):
    self.trace_content = '{class_name}:{line_num}'
    self.trace_formatter = self._lineNumLogFormatter
    return 'TestTraceEvent.{call}("%s");' % self.trace_content

  def _traceEveryStatement(self, token, trace_template):
    if type(token) == antlr4.tree.Tree.TerminalNodeImpl:
      return
    for c in token.getChildren():
      if type(c) == JavaParser.BlockStatementContext:
        begin_trace_insertion = self.trace_formatter(trace_template, c, 'begin')
        end_trace_insertion = self.trace_formatter(trace_template, c, 'end')
        self.refactor.insertBeforeToken(c, begin_trace_insertion, use_mask=True)
        self.refactor.insertAfterToken(c, end_trace_insertion, use_mask=True)
      self._traceEveryStatement(c, trace_template)

  def _getTraceEveryStatementFn(self, trace_template):
    def _inner(token):
      self._traceEveryStatement(token, trace_template)
    return _inner


class JavaStats(JavaRefactorAgent):
  """Print basic stats for a given java file"""
  pass
