import re
import logging
import collections
import functools
import subprocess

from antlr.PythonParserListener import PythonParserListener
from antlr.PythonLexer import PythonLexer
from antlr.PythonParser import PythonParser

from agents.Refactor import Refactor

class PythonAgentBase(PythonParserListener):
  @staticmethod
  def createLexer(input_stream):
    return PythonLexer(input_stream)

  @staticmethod
  def createParser(token_stream):
    return PythonParser(token_stream)

  @staticmethod
  def defaultEntryPoint(parser):
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
    if not filename.endswith('.java'):
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


