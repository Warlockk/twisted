# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.
#

"""
Tests for L{twisted.trial.util}
"""

from twisted.trial.unittest import TestCase
from unittest import skipIf



@skipIf(True, "Skip all tests when @skipIf is used on a class")
class SkipDecoratorUsedOnClass(TestCase):
    """
    All tests should be skipped because @skipIf decorator is used on
    this class.
    """

    def test_shouldNeverRun_1(self):
        raise Exception("Test should skip and never reach here")


    def test_shouldNeverRun_2(self):
        raise Exception("Test should skip and never reach here")



class SkipDecoratorUsedOnMethods(TestCase):
    """
    Only methods where @skipIf decorator is used should be skipped.
    """

    @skipIf(True, "skipIf decorator used so skip test")
    def test_shouldNeverRun(self):
        raise Exception("Test should skip and never reach here")


    def test_shouldShouldRun(self):
        self.assertTrue(True, "Test should run and not be skipped")



class SkipAttributeOnClass(TestCase):
    """
    All tests should be skipped because skip attribute is set on
    this class.
    """

    skip = "'skip' attribute set on this class, so skip all tests"

    def test_one(self):
        raise Exception("Test should skip and never reach here")


    def test_two(self):
        raise Exception("Test should skip and never reach here")



class SkipAttributeOnMethods(TestCase):
    """
    Only methods where @skipIf decorator is used should be skipped.
    """

    def test_one(self):
        raise Exception("Should never reach here")

    test_one.skip = "skip test, skip attribute set on method"  # type: ignore[attr-defined]  # noqa


    def test_shouldNotSkip(self):
        self.assertTrue(True, "Test should run and not be skipped")
