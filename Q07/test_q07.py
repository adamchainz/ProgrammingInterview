# coding=utf-8
import unittest

from q07 import first_index


class Q7Tests(unittest.TestCase):
    def test_no_duplicates(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(first_index(numbers, 3, 0, len(numbers)-1), 2)

    def test_some_duplicates(self):
        numbers = [1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(first_index(numbers, 3, 0, len(numbers)-1), 3)

    def test_all_duplicates(self):
        numbers = [3, 3, 3, 3, 3, 3, 3, 3, 3]
        self.assertEqual(first_index(numbers, 3, 0, len(numbers)-1), 0)

    def test_not_found(self):
        numbers = [1, 2, 4, 5, 6, 7, 8, 9]
        self.assertEqual(first_index(numbers, 3, 0, len(numbers)-1), -1)


if __name__ == '__main__':
    unittest.main()
