# coding=utf-8
import unittest

from q33 import reverse


class Q33Tests(unittest.TestCase):
    def test_empty(self):
        my_list = []
        reverse(my_list)
        self.assertEqual(my_list, [])

    def test_single(self):
        my_list = [1]
        reverse(my_list)
        self.assertEqual(my_list, [1])

    def test_double(self):
        my_list = [1, 2]
        reverse(my_list)
        self.assertEqual(my_list, [2, 1])

    def test_long_even(self):
        my_list = [1, 2, 3, 4, 5, 6, 7, 8]
        reverse(my_list)
        self.assertEqual(my_list, [8, 7, 6, 5, 4, 3, 2, 1])

    def test_long_odd(self):
        my_list = [1, 2, 3, 4, 5, 6, 7]
        reverse(my_list)
        self.assertEqual(my_list, [7, 6, 5, 4, 3, 2, 1])


if __name__ == '__main__':
    unittest.main()
