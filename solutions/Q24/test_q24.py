# coding=utf-8
import unittest

from q24 import balance_point


class Q24Tests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(balance_point([]), None)

    def test_example(self):
        self.assertEqual(balance_point([1, 2, 9, 4, -1]), 2)

    def test_simple(self):
        self.assertEqual(balance_point([1, 2, 1]), 1)

    def test_0_one_side(self):
        self.assertEqual(balance_point([1, 0]), 0)
        self.assertEqual(balance_point([0, 1]), 1)

    def test_finds_first(self):
        self.assertEqual(balance_point([2, 4, 0, 0, 0, 2, 4]), 2)


if __name__ == '__main__':
    unittest.main()
