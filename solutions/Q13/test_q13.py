# coding=utf-8
import unittest

from q13 import all_pairs_summing


class Q13Tests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(all_pairs_summing([], 0), [])
        self.assertEqual(all_pairs_summing([], 1), [])
        self.assertEqual(all_pairs_summing([], 10), [])

    def test_simple(self):
        self.assertEqual(all_pairs_summing([1, 2], 1), [])
        self.assertEqual(all_pairs_summing([1, 2], 2), [])
        self.assertEqual(all_pairs_summing([1, 2], 3), [(1, 2)])

    def test_bigger(self):
        self.assertEqual(
            all_pairs_summing([1, 2, 2, 3], 4),
            [(1, 3), (2, 2)]
        )
        self.assertEqual(
            all_pairs_summing([1, 2, 2, 3], 3),
            [(1, 2)]
        )
        self.assertEqual(
            all_pairs_summing([1, 2, 2, 3], 40),
            []
        )

    def test_large(self):
        self.assertEqual(
            all_pairs_summing([1, 2, 3, 4, 5, 6, 7, 8], 9),
            [(1, 8), (2, 7), (3, 6), (4, 5)]
        )


if __name__ == '__main__':
    unittest.main()
