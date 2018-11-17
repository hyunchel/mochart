"""Run tests on documentation tests(doctest).

Currently setup this way b/c pytest does not support "load_tests" protocol.
"""
import unittest

import doctest

import mochart.utils


def load_tests(loader, tests, ignore):
    """Load doctests as unit test suite."""
    tests.addTests(doctest.DocTestSuite(mochart.utils))
    return tests


if __name__ == "__main__":
    unittest.main()
