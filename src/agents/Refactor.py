import collections

class Refactor(object):
  def __init__(self, filename, save_as_new):
    self._offset_table = collections.defaultdict(int)
    self._filename = filename
    with open(filename, 'r') as f:
      self._content = f.read()
    self._save_as_new = save_as_new

  @property
  def offset_table(self):
    return self._offset_table

  @property
  def content(self):
    return self._content

  def GetStartLocation(self, token):
    return self._GetLexPosRealLocation(token.start.start)

  def GetStopLocation(self, token):
    return self._GetLexPosRealLocation(token.stop.stop)

  def _GetLexPosRealLocation(self, lexpos):
    offset = 0
    for i,j in self.offset_table.items():
      if i < lexpos:
        offset += j
    return lexpos + offset

  def GetStartStop(self, token):
    return self.GetStartLocation(token), self.GetStopLocation(token)

  def RemoveToken(self, token):
    start, stop = self.GetStartStop(token)
    self.content = self.content[:start] + self.content[stop:]
    self.offset_table[start] = stop-start

  def ReplaceToken(self, token, replacement):
    start, stop = self.GetStartStop(token)
    self.content = self.content[:start] + replacement + self.content[stop:]

  def InsertAboveToken(self, token):
    pass

  def InsertBelowToken(self, token):
    pass

  def InsertInFrontOfToken(self, token):
    pass

  def InsertRightAfterToken(self, token):
    pass

  def ActionOnX(self, tb, ctx_class, condition_fn=None, action_fn=None,
                optional=False):
    if not condition_fn:
      condition_fn = lambda _ : True
    x_list = tb.get(ctx_class)
    if x_list:
      limited_list = [i for i in x_list if condition_fn(i)]
      if action_fn:
        for i in limited_list:
          action_fn(i)
      return limited_list
    else:
      if optional:
        return []
      else:
        raise Exception('Did not find any of this type of element in code: %s'
                        % str(ctx_class))


  def Save(self):
    filename = self._filename
    if self._save_as_new:
      filename += '.new'
    with open(filename, 'w') as f:
      f.write(self.content)
