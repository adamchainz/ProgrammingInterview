# coding=utf-8
import unittest
from q02 import my_square_root


class Q02Tests(unittest.TestCase):
    def test_basic_squares(self):
        self.assertAlmostEqual(my_square_root(1), 1, 4)
        self.assertAlmostEqual(my_square_root(4), 2, 4)
        self.assertAlmostEqual(my_square_root(9), 3, 4)
        self.assertAlmostEqual(my_square_root(16), 4, 4)

    def test_irrational_roots(self):
        self.assertAlmostEqual(my_square_root(2), 1.41419, 4)
        self.assertAlmostEqual(my_square_root(5), 2.23607, 4)

    def test_less_than_one(self):
        self.assertAlmostEqual(my_square_root(0.25), 0.5, 4)
        self.assertAlmostEqual(my_square_root(0.05), 0.22361, 4)

if __name__ == '__main__':
    unittest.main()
