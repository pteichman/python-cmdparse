import unittest
from cmdparse import Command, CommandParser

import testCommands

class testCmdparse(unittest.TestCase):
    def setUp(self):
        self.parser = CommandParser()
        self.parser.add_commands(testCommands)

    def tearDown(self):
        del self.parser

    def testEcho(self):
        (command, options, args) = self.parser.parse_args("echo foo".split())

        self.assert_(isinstance(command, testCommands.EchoCommand))

test_suite = unittest.TestSuite()
test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCmdparse))
