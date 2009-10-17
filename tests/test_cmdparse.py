import unittest
from cmdparse import Command, CommandParser

class testCmdparse(unittest.TestCase):
    pass

test_suite = unittest.TestSuite()
test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCmdparse))
