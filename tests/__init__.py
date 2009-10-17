import unittest

__ALL__ = ["cmdparse_suite"]

# import our test modules
import test_cmdparse

cmdparse_suite = unittest.TestSuite()
cmdparse_suite.addTest(unittest.defaultTestLoader.loadTestsFromModule(test_cmdparse))
