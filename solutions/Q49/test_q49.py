# coding=utf-8
import unittest

from q49 import longest_increasing_subs


class Q49Tests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(longest_increasing_subs([]), [])

    def test_single(self):
        self.assertEqual(longest_increasing_subs([3]), [3])

    def test_double_up(self):
        self.assertEqual(longest_increasing_subs([1, 3]), [1, 3])

    def test_double_down(self):
        self.assertEqual(longest_increasing_subs([3, 1]), [3])

    def test_example(self):
        self.assertEqual(
            longest_increasing_subs([2, 6, 4, 5, 1, 3]),
            [2, 4, 5]
        )

    def test_longer(self):
        self.assertEqual(
            longest_increasing_subs([1, 2, 3, 4, 5, 1]),
            [1, 2, 3, 4, 5]
        )

    def test_longer2(self):
        self.assertEqual(
            longest_increasing_subs([1, 7, 3, 4, 5, 1]),
            [1, 3, 4, 5]
        )

    def test_longer3(self):
        self.assertEqual(
            longest_increasing_subs([1, 7, 9, 8, 3, 4, 5, 1]),
            [1, 3, 4, 5]
        )

    def test_descending(self):
        self.assertEqual(
            longest_increasing_subs([7, 6, 5, 4, 3, 2, 1]),
            [7]
        )


if __name__ == '__main__':
    unittest.main()
