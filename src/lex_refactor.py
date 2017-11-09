#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

import sys
if sys.version_info[0] < 3:
    raise "Must be using Python 3"
import logging
import argparse
import os
import re

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from antlr.JavaLexer import JavaLexer
from antlr.JavaParser import JavaParser
from antlr.JavaParserListener import JavaParserListener

from agents.JavaAgents import AndroidJavaLogAgent, AndroidJavaTraceAgent, JavaStats
from agents.CppAgents import CppStats, CppLogAgent
from agents.JavaScriptAgents import JavaScriptStats, JavaScriptLogAgent
from agents.PythonAgents import PythonStats, PythonLogAgent

_AGENT_DICT = {
    'android-add-log': AndroidJavaLogAgent,
    'android-add-trace': AndroidJavaTraceAgent,
    'cpp-add-log': CppLogAgent,
    'python-add-log': PythonLogAgent,
    'javascript-add-log': JavaScriptLogAgent,
    'java-stats': JavaStats,
    'cpp-stats': CppStats,
    'python-stats': PythonStats
}

def ActionOnDirectory(agent, directory, pattern=None,
                      logging_level=logging.WARNING):
  """Use agent on all the files in a directory that matches pattern"""
  if pattern is not None:
    file_pattern = re.compile(pattern)
  for (dirpath, _, filenames) in os.walk(directory):
    for filename in filenames:
      whole_path = os.path.join(dirpath, filename)
      if pattern is not None and not file_pattern.match(whole_path):
        logging.info('Skip %s' % filename)
      else:
        ActionOnFile(agent, whole_path, logging_level)


def ActionOnFile(agent, filename, logging_level=logging.WARNING):
  """Use agent on one file"""
  logger = SetLogger(logging_level, filename)
  if agent.skip(filename):
    logger.warning('%s does not match %s requirement' % (filename, agent))
  inp = FileStream(filename)
  agent.set_file(filename)
  lexer = agent.createLexer(inp)
  stream = CommonTokenStream(lexer)
  parser = agent.createParser(stream)
  tree = agent.defaultEntryPoint(parser)
  walker = ParseTreeWalker()
  walker.walk(agent, tree)
  agent.setup()
  agent.actions()


def SetLogger(logging_level, filepath):
  log = logging.getLogger()
  filename = filepath.split('/')[-1]
  f = logging.Formatter(
      filename + ':%(levelname)s:%(module)s:%(lineno)s: %(message)s')
  fh = logging.StreamHandler()
  fh.setLevel(logging_level)
  fh.setFormatter(f)
  log.propagate = False
  if len(log.handlers) > 0:
    log.removeHandler(log.handlers[0])
  log.setLevel(logging_level)
  log.addHandler(fh)
  return log

def Main():
  argument_parser = argparse.ArgumentParser(add_help=False)
  list_agent_parser = argparse.ArgumentParser(add_help=False)
  argument_parser.add_argument(
      choices=list(_AGENT_DICT.keys()), dest='agent',
      help='Specify the agent for the current file or directory. Use `-l` to '
           'list agents and `[agent-name] -h` to find out agent specific '
           'arguments')
  argument_parser.add_argument('-p', '--pattern', help='Pattern for matching '
      'files in directory, if not specified, it will match all the files'
      ' in the directory')
  argument_parser.add_argument('-f', '--file', help='Specify file')
  argument_parser.add_argument('-d', '--directory',
                               help='Specify directory')
  argument_parser.add_argument('-v', '--verbose', help='Log info',
                               action='store_true')
  list_agent_parser.add_argument('-l', '--list-agents', action='store_true')
  argument_parser.add_argument(
      '-l', '--list-agents', help='List all available agents',
      action='store_true', default=False)
  argument_parser.add_argument('-n', '--save-as-new', default=False,
                               action='store_true', help='Save as a new file')
  argument_parser.add_argument('-c', '--clean', action='store_true',
      default=False, help='Clean all the previously inserted content')

  list_agent_args, _ = list_agent_parser.parse_known_args()
  if list_agent_args.list_agents:
    print('Available agents and description:\n')
    for agent, agent_class in _AGENT_DICT.items():
      print("%25s:\t%s" % (
        agent, agent_class.__doc__.strip()
        if agent_class.__doc__ is not None else 'N.A.'))
    return

  arguments, _ = argument_parser.parse_known_args()

  argument_parser = argparse.ArgumentParser(
      add_help=True, parents=[argument_parser])
  agent_class = _AGENT_DICT[arguments.agent]
  argument_parser = agent_class.addOptions(argument_parser)

  try:
    import argcomplete
    argcomplete.autocomplete(argument_parser)
  except ImportError:
    logging.error('Can not import argcomplete')

  arguments = argument_parser.parse_args()

  logging_level = logging.WARN
  if arguments.verbose:
    logging_level = logging.INFO

  if arguments.file and arguments.directory:
    raise Exception(
        'Can not specify --file and --directory at the same time')

  if arguments.file is None and arguments.directory is None:
    raise Exception(
        'Must at least specify --file or --directory')

  agent = agent_class(arguments)

  if arguments.clean:
    agent.clean()
    return
  agent.validate()
  if arguments.file:
    ActionOnFile(agent, arguments.file, logging_level)
  else:
    ActionOnDirectory(agent, arguments.directory, pattern=arguments.pattern,
                      logging_level=logging_level)

if __name__ == '__main__':
    Main()
