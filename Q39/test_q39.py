# coding=utf-8
import unittest

from q39 import max_rect


class Q39Tests(unittest.TestCase):
    def test_single(self):
        self.assertEqual(max_rect([2]), 2)

    def test_0(self):
        self.assertEqual(max_rect([2, 0]), 2)

    def test_steps(self):
        self.assertEqual(max_rect([1, 2, 2.9]), 4)

    def test_example(self):
        self.assertEqual(max_rect([2, 4, 2, 1]), 6)

    def test_with_gaps(self):
        self.assertEqual(max_rect([0, 1, 2, 0, 2, 3, 0, 0, 0]), 4)


if __name__ == '__main__':
    unittest.main()
