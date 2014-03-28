# coding=utf-8
import unittest

from q16 import max_consecutive_sum


class Q16Tests(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(max_consecutive_sum([]), 0)
        self.assertEqual(max_consecutive_sum([1]), 1)
        self.assertEqual(max_consecutive_sum([-1]), -1)

    def test_example(self):
        self.assertEqual(max_consecutive_sum([-1, 2, 3, 5, -2]), 10)

    def test_big_alternating(self):
        self.assertEqual(max_consecutive_sum([-1, 1] * 100), 1)
        self.assertEqual(max_consecutive_sum([-1, 1, 2, -2] * 100), 3)

    def test_all_negative(self):
        self.assertEqual(max_consecutive_sum([-1, -2, -3, -4]), -1)

if __name__ == '__main__':
    unittest.main()
