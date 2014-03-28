# coding=utf-8
import unittest

from q18 import num_rotations_til_sorted


class Q18Tests(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(num_rotations_til_sorted([]), 0)
        self.assertEqual(num_rotations_til_sorted([1]), 0)
        self.assertEqual(num_rotations_til_sorted([1, 99]), 0)
        self.assertEqual(num_rotations_til_sorted([1, 99, 101]), 0)
        self.assertEqual(num_rotations_til_sorted(list(range(1000))), 0)

        self.assertEqual(num_rotations_til_sorted([99, 1]), 1)

    def test_example(self):
        self.assertEqual(num_rotations_til_sorted([3, 4, 5, 1, 2]), 2)

    def test_repeats(self):
        self.assertEqual(num_rotations_til_sorted([4, 5, 1, 2, 3]), 2)
        self.assertEqual(num_rotations_til_sorted([4, 5, 1, 2, 3, 3]), 2)
