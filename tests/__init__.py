import unittest

__ALL__ = ["cmdparse_suite"]

import test_cmdparse

loader = unittest.TestLoader()

cmdparse_suite = unittest.TestSuite()
cmdparse_suite.addTest(loader.loadTestsFromModule(test_cmdparse))
