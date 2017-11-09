#!/usr/bin/env python

import src.agents.JavaAgents as ja

import unittest
from mock import patch

class Test(unittest.TestCase):
  def setUp(self):
    self.test_string ='''     @Override
      protected void setUp() throws Exception {
          super.setUp();
          mTestController = new TestController();
          injectObjectAndReload(mTestController, "testController");
      }'''

  def testInsertLogEveryLine(self):
    pattern = ' protected '
    replacement = ' public '
    expected_result = '''     @Override
      public void setUp() throws Exception {
          super.setUp();
          mTestController = new TestController();
          injectObjectAndReload(mTestController, "testController");
      }'''
    self.assertEqual(
        expected_result, auto_change._ReturnReplacement(
            pattern, replacement, self.test_string))

