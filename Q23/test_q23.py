# coding=utf-8
import unittest

from q23 import maximal_submatrix_sum


class Q23Tests(unittest.TestCase):
    def test_one_by_one(self):
        self.assertEqual(maximal_submatrix_sum([[97]]), 97)

    def test_two_by_two(self):
        self.assertEqual(maximal_submatrix_sum([[97, -4], [-3, -23]]), 97)

    def test_row(self):
        self.assertEqual(maximal_submatrix_sum([[79, -4, -38]]), 79)

    def test_column(self):
        self.assertEqual(maximal_submatrix_sum([[44], [22], [-81]]), 66)

    def test_example(self):
        self.assertEqual(
            maximal_submatrix_sum([[1, 2, 3], [-1, -2, -3], [0, 0, 0]]),
            6
        )

    def test_example2(self):
        self.assertEqual(
            maximal_submatrix_sum([[1, -1, 0], [2, -2, 0], [3, -3, 0]]),
            6
        )

    def test_giant(self):
        self.assertEqual(
            maximal_submatrix_sum([range(99), range(-99, 0)]),
            sum(range(99))
        )


if __name__ == '__main__':
    unittest.main()
