# coding=utf-8
import unittest

from q05 import to_rational


class Q5Tests(unittest.TestCase):
    def test_between_zero_and_one(self):
        self.assertEqual(to_rational(0.125), '1/8')

    def test_between_zero_and_minus_one(self):
        self.assertEqual(to_rational(-0.125), '-1/8')

    def test_larger_than_one(self):
        self.assertEqual(to_rational(3.25), '13/4')

    def test_smaller_than_minus_one(self):
        self.assertEqual(to_rational(-8.9), '-89/10')


if __name__ == '__main__':
    unittest.main()
