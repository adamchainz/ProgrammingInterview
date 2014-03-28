# coding=utf-8
import unittest

from q03 import count_in_sorted


class Q03Tests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(count_in_sorted(2, []), 0)

    def test_single(self):
        self.assertEqual(count_in_sorted(2, [2]), 1)

    def test_double(self):
        self.assertEqual(count_in_sorted(2, [4, 1]), 0)
        self.assertEqual(count_in_sorted(2, [2, 4]), 1)
        self.assertEqual(count_in_sorted(2, [2, 2]), 2)

    def test_triple(self):
        self.assertEqual(count_in_sorted(2, [1, 4, 9]), 0)
        self.assertEqual(count_in_sorted(2, [1, 2, 7]), 1)
        self.assertEqual(count_in_sorted(2, [-22, 2, 2]), 2)

    def test_example(self):
        self.assertEqual(count_in_sorted(2, [1, 2, 2, 2, 3, 4]), 3)

    def test_missing(self):
        self.assertEqual(count_in_sorted(77, [1, 2, 2, 2, 3, 4]), 0)

    def test_really_long(self):
        long_list = [1, 1, 1] + [4] * 9999
        self.assertEqual(count_in_sorted(7, long_list), 0)
        self.assertEqual(count_in_sorted(1, long_list), 3)
        self.assertEqual(count_in_sorted(4, long_list), 9999)


if __name__ == '__main__':
    unittest.main()
