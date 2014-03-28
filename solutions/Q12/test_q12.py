# coding=utf-8
import unittest

from q12 import merge_sorted_lists


class Q12Tests(unittest.TestCase):
    def test_empties(self):
        self.assertEqual(merge_sorted_lists([], []), [])
        self.assertEqual(merge_sorted_lists([1, 2], []), [1, 2])
        self.assertEqual(merge_sorted_lists([], [5, 6]), [5, 6])

    def test_no_interleaving(self):
        self.assertEqual(
            merge_sorted_lists([1, 2], [5, 6]),
            [1, 2, 5, 6]
        )

    def test_interleaving(self):
        self.assertEqual(
            merge_sorted_lists([1, 3, 5], [2, 4]),
            [1, 2, 3, 4, 5]
        )

if __name__ == '__main__':
    unittest.main()
