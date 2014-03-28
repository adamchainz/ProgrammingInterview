# coding=utf-8
import unittest
from q42 import subsets


class Q42Tests(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(
            subsets([1], 0),
            set()
        )

    def test_single(self):
        self.assertEqual(
            subsets([1], 1),
            set([(1,)])
        )

    def test_two(self):
        self.assertEqual(
            subsets([1, 2, 3], 2),
            set([(1, 2), (1, 3), (2, 3)])
        )

    def test_three(self):
        self.assertEqual(
            subsets([1, 2, 3], 3),
            set([(1, 2, 3)])
        )

if __name__ == '__main__':
    unittest.main()
