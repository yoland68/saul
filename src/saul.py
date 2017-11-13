#!/usr/bin/env python

import sys
if sys.version_info[0] < 3:
    raise "Must be using Python 3"
else:
  import lex_refactor

if __name__ == '__main__':
  lex_refactor.Main()
