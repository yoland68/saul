from agents.CppAgentBase import CppAgentBase, CppRefactorAgent

class CppStats(CppAgentBase):
  """Show basic stats of the cpp (Not implemented yet)"""
  pass

class CppLogAgent(CppRefactorAgent):
  """Not yet implemented"""

  #Override
  def validate(self):
    pass

  def actions(self):
    import ipdb
    ipdb.set_trace()
