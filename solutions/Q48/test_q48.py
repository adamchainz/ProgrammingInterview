# coding=utf-8
import unittest

from q48 import max_subsequent_product


class Q48Tests(unittest.TestCase):
    def test_all_positive(self):
        numbers = [2, 2, 2, 2, 2, 2]
        self.assertEqual(max_subsequent_product(numbers), 64)

    def test_all_negative(self):
        numbers = [-2, -2, -2, -2, -2, -2]
        self.assertEqual(max_subsequent_product(numbers), 64)

    def test_with_zeros(self):
        numbers = [2, 2, 2, 0, 2, 2]
        self.assertEqual(max_subsequent_product(numbers), 8)

    def test_with_negatives(self):
        numbers = [2, 2, 2, -2, 2, 2]
        self.assertEqual(max_subsequent_product(numbers), 8)

    def test_with_all(self):
        numbers = [2, 0, 2, 2, -2, 2]
        self.assertEqual(max_subsequent_product(numbers), 4)


if __name__ == '__main__':
    unittest.main()
