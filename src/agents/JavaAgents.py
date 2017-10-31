from antlr.JavaParser import JavaParser

from agents.JavaAgentBase import JavaAgentBase

class JavaLogAgent(JavaRefactorAgent):
  @staticmethod
  def addOptions(parser):
    parser.add_argument('--method', help='Specify the method name')
    parser.add_argument(
        '--each-line', action-help='Add logging in between each statement')
    parser.add_argument(
        '--tag', help='Specify the tag used for logging')

  def actions(self):
    for m in self.tb[JavaParser.MethodDeclarationContext]:
      self.refactor.

class JavaTraceAgent(JavaRefactorAgent):

