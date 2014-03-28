# coding=utf-8
import unittest

from q17 import my_division


class Q17Tests(unittest.TestCase):
    def test_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            my_division(1, 0)

    def test_self(self):
        self.assertEqual(my_division(4, 4), 1)

    def test_double(self):
        self.assertEqual(my_division(4, 2), 2)

    def test_less_than(self):
        self.assertEqual(my_division(77, 99), 0)

    def test_odd(self):
        self.assertEqual(my_division(33, 2), 16)

    def test_huge(self):
        self.assertEqual(my_division(9000000, 2), 4500000)


if __name__ == '__main__':
    unittest.main()
