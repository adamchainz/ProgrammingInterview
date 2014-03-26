# coding=utf-8
import unittest

from q07 import first_index


class Q07Tests(unittest.TestCase):
    def test_no_duplicates(self):
        self.assertEqual(first_index([1, 2, 3, 4, 5, 6, 7, 8, 9], 3), 2)

    def test_some_duplicates(self):
        numbers = [1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(first_index(numbers, 3), 3)

    def test_all_duplicates(self):
        numbers = [3, 3, 3, 3, 3, 3, 3, 3, 3]
        self.assertEqual(first_index(numbers, 3), 0)

    def test_not_found(self):
        numbers = [1, 2, 4, 5, 6, 7, 8, 9]
        self.assertEqual(first_index(numbers, 3), None)


if __name__ == '__main__':
    unittest.main()
