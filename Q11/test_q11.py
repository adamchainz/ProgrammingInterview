# coding=utf-8
import unittest

from q11 import subsets


class Q11Tests(unittest.TestCase):
    def test_zero(self):
        self.assertSetEqual(
            subsets([]),
            set([()])
        )

    def test_single(self):
        self.assertSetEqual(
            subsets([1]),
            set([(), (1,)])
        )

    def test_two(self):
        self.assertSetEqual(
            subsets([1, 2]),
            set([(), (1,), (2,), (1, 2)])
        )

    def test_three(self):
        self.assertSetEqual(
            subsets([1, 2, 3]),
            set([(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)])
        )

if __name__ == '__main__':
    unittest.main()
