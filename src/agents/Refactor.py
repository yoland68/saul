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

  def Save(self):
    filename = self._filename
    if self._save_as_new:
      filename += '.new'
    with open(filename, 'w') as f:
      f.write(self.content)
