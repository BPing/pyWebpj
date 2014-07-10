# __author__ = 'ming'
# coding=utf-8


import unittest
import os
import sys

here = os.path.dirname(__file__)


def test_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    for fn in os.listdir(here):
        if fn.startswith("test") and fn.endswith(".py"):
            modname = "conn.tests." + fn[:-3]
            __import__(modname)
            module = sys.modules[modname]
            suite.addTests(loader.loadTestsFromModule(module))
    return suite


def main():
    suite = test_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    main()
