import sys
import re
import logging
import antlr4
import subprocess

from antlr.JavaParser import JavaParser

from agents.JavaAgentBase import GetIsJavaMcFn, JavaAgentBase, JavaRefactorAgent

def _AddDefaultArguments(parser, keyword):
  parser.add_argument(
      '--method-declaration',
      help='Specify the method declarition name, e.g. `--method-declaration '
           'func would %s inside the statments inside func declaration'
           % keyword)
  parser.add_argument(
      '--method-invocation',
      help='Specify the method invocation name, e.g. `--method-invocation'
           ' func would %s before each call'
           % keyword)
  parser.add_argument(
      '--%s-each-line' % keyword, action='store_true', default=False,
      help='Add %s in between each statement' % keyword)
  parser.add_argument(
      '--%s-entry-exit' % keyword, action='store_true', default=False,
      help='Add %s only at block entry and exit' % keyword)
  return parser


class JavaLogAgent(JavaRefactorAgent):
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
        '--log-count', action='store_true', default=False,
        help='Use number counting in log content')
    parser.add_argument(
        '--log-line', action='store_true', default=False,
        help='Use file line number in log content')
    parser.add_argument(
        '--log-source', action='store_true', default=False,
        help='Use source code itself as log content')
    parser.add_argument(
        '--bring-your-own-log', help='Specify your own log statement, e.g.'
        ' --bring-your-own-log=Log.d("#SAUL", Integer.toString(mInt))')
    parser.add_argument(
        '--tag', default='#SAUL', help='Specify the tag used for logging')
    parser.add_argument(
        '--call', default='d', choices=['d', 'i', 'w', 'e'],
        help='Specify which log method to use [d, i, w, e]. `d` is default')
    parser.add_argument(
        '--package', default='org.chromium.base.Log',
        help='Specify which logging package to use')
    return parser

  def __init__(self, args):
    super(JavaLogAgent, self).__init__(args)
    self.log_content = None
    self.log_formatter = None
    self.counter = 0

  #Override
  def validate(self):
    if self.args.log_each_line and self.args.log_entry_exit:
      raise Exception('Can not specify --log-each-line and --log-entry-exit at '
                      'the same time')

    if self.args.log_count and self.args.log_line:
      raise Exception(
          'Can not specify --log-count and --log-line at the same time')

  #Override
  def actions(self):
    if self.args.clean:
      return
    log_template = self.getLogStatement()
    self.addImport(self.args.package)
    if self.args.method_declaration:
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
        ' ' * token.depth() + self.refactor.content[token.start.start:token.stop.stop+1])
    code = code.split('\n')[0]
    code = code.replace('"', r'\"')
    return template.format(
      class_name=self.class_name, line_num=line_num, code=code)

  def getLogStatement(self):
    if self.log_content is None:
      if self.args.bring_your_own_log:
        self.log_content = self.args.bring_your_own_log
        self.log_formatter = lambda tem, _: tem
      if self.args.log_count:
        self.log_content = "{class_name}:{counter:d}"
        self.log_formatter = self._counterLogFormatter
      elif self.args.log_line:
        self.log_content = "{class_name}:{line_num}"
        self.log_formatter = self._lineNumLogFormatter
      elif self.args.log_source:
        self.log_content = "{class_name}:\\t{code}"
        self.log_formatter = self._sourceLogFormatter
      # default choice
      else:
        self.log_content = "{class_name}"
        self.log_formatter = self.
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

class JavaTraceAgent(JavaRefactorAgent):
  """Add Tracing to Java Method or Classes"""
  @staticmethod
  def addOptions(parser):
    parser = _AddDefaultArguments(parser, 'trace')
    return parser

  #Override
  def validate(self):
    pass

  def actions(self):
    self.validate()
    trace_insertion = self.getTraceStatement()
    if self.args.method_declaration:
      self.refactor.actionOnX(
          self.tb, JavaParser.MethodDeclarationContext,
          condition_fn = lambda x: x.IDENTIFIER == self.args.method_declaration,
          action_fn = self.traceEveryLine)
    elif self.args.method_invocation:
      self.refactor.actionOnX(
          self.tb, JavaParser.BlockStatementContext,
          condition_fn = lambda x: self.args.method_invocation+'(' in x.getText(),
          action_fn = self.traceInvocation)
    else:
      logging.error('Nothing happened')

  def getTraceStatment(self):
    pass


class JavaStats(JavaRefactorAgent):
  """Print basic stats for a given java file"""
  pass
