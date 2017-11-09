import logging
import inspect
import collections

def _CompareToken(t1, t2):
  if t1.start.start == t2.start.start:
    return 0
  elif t1.start.start > t2.start.start:
    return 1
  else:
    return -1

class Refactor(object):
  def __init__(self, filename, save_as_new, start_mask='', end_mask=''):
    self._offset_table = collections.defaultdict(int)
    self._filename = filename
    self._start_mask = start_mask
    self._end_mask = end_mask
    with open(filename, 'r') as f:
      self.content = f.read()
    self._change_dict = {}
    self._save_as_new = save_as_new

  @property
  def change_dict(self):
    return self._change_dict

  @property
  def offset_table(self):
    return self._offset_table

  @property
  def start_mask(self):
    return self._start_mask

  @property
  def end_mask(self):
    return self._end_mask

  def getStartLocation(self, token):
    return self._GetLexPosRealLocation(token.start.start)

  def getStopLocation(self, token):
    return self._GetLexPosRealLocation(token.stop.stop)

  def _GetLexPosRealLocation(self, lexpos):
    offset = 0
    for i,j in self.offset_table.items():
      if i < lexpos:
        offset += j
    return lexpos + offset

  def getStartStop(self, token):
    return self.GetStartLocation(token), self.GetStopLocation(token)

  def removeToken(self, token):
    original_start = token.start.start
    start, stop = self.GetStartStop(token)
    self.content = self.content[:start] + self.content[stop:]
    self.offset_table[original_start] = start-stop

  def replaceToken(self, token, replacement):
    original_start = token.start.start
    start, stop = self.GetStartStop(token)
    self.content = self.content[:start] + replacement + self.content[stop:]
    self.offset_table[original_start] = len(replacement) - (stop-start)

  def insertBeforeToken(self, token, insertion, use_mask=True):
    #STUB: find an effective way to insert that handles new lines
    if use_mask:
      insertion = self.start_mask + insertion + self.end_mask
    self.change_dict[token.start.start] = insertion

  def deprInsertBeforeToken(self, token, insertion, use_mask=True):
    #STUB: find an effective way to insert that handles new lines
    if use_mask:
      insertion = self.start_mask + insertion + self.end_mask
    original_start = token.start.start
    start = self.getStartLocation(token)
    self.content = self.content[:start] + insertion + self.content[start:]
    self.offset_table[original_start] = len(insertion)

  def insertAfterToken(self, token, insertion, use_mask=True):
    #STUB: find an effective way to insert that handles new lines
    if use_mask:
      insertion = self.start_mask + insertion + self.end_mask
    self.change_dict[token.stop.stop+1] = insertion

  def deprInsertAfterToken(self, token, insertion, use_mask=True):
    #STUB: find an effective way to insert that handles new lines
    if use_mask:
      insertion = self.start_mask + insertion + self.end_mask
    original_stop = token.stop.stop
    stop = self.getStopLocation(token)
    self.content = self.content[:stop+1] + insertion + self.content[1+stop:]
    self.offset_table[original_stop] = len(insertion)

  #TODO: refactor this to be a outer function
  def getInsertBeforeTokenFn(self, insertion, use_mask=True):
    def _inner_function(token):
      self.insertBeforeToken(token, insertion, use_mask)
    return _inner_function

  #TODO refactor tb to be a inner object
  #TODO remove debugger
  def actionOnX(self, tb, ctx_class, condition_fn=None, action_fn=None,
                optional=False, warn=True, debug=False):
    if debug == True:
      import ipdb
      ipdb.set_trace()
    if not condition_fn:
      condition_fn = lambda _ : True
    x_list = tb.get(ctx_class)
    if x_list:
      limited_list = [i for i in x_list if condition_fn(i)]
      if warn and not limited_list:
        logging.warn(
            '%s is not found under the required condition, condition fn:\n%s'
            % (str(ctx_class), ''.join(
                inspect.getsourcelines(condition_fn)[0])))
      if action_fn:
        for i in limited_list:
          action_fn(i)
      return limited_list
    else:
      if warn:
        logging.warn('%s is not found in this file' % str(ctx_class))
      if optional:
        return []
      else:
        raise Exception('Did not find any of this type of element in code: %s'
                        % str(ctx_class))

  def save(self):
    for i in sorted(self.change_dict.keys(), reverse=True):
      self.content = self.content[:i] + self.change_dict[i] + self.content[i:]
    filename = self._filename
    if self._save_as_new:
      filename += '.new'
    with open(filename, 'w') as f:
      f.write(self.content)
