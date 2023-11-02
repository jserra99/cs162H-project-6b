# Author: Joseph Serra
# GitHub username: jserra99
# Date: 11/2/2023
# Description: Project-6b; Is Decreasing Tester

import unittest
from is_decreasing import is_decreasing


class TestIsDecreasing(unittest.TestCase):

    def test_is_decreasing(self):
        """ Test is_decreasing() """
        list_one = [65, 59, 43, 22, 10, 3]
        self.assertTrue(is_decreasing(list_one))
        list_two = [47, 45, 22, 22, 10]
        self.assertFalse(is_decreasing(list_two))
        list_three = [33, 32, 29, 31]
        self.assertFalse(is_decreasing(list_three))
