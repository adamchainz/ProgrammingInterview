# coding=utf-8
import unittest

from q10 import is_rotated_palindrome


class Q10Tests(unittest.TestCase):
    def test_base(self):
        self.assertTrue(is_rotated_palindrome(''))
        self.assertTrue(is_rotated_palindrome('1'))

    def test_nonpalindromes(self):
        self.assertFalse(is_rotated_palindrome('123'))
        self.assertFalse(is_rotated_palindrome('321'))
        self.assertFalse(is_rotated_palindrome('1234'))
        self.assertFalse(is_rotated_palindrome('duckyduck'))

    def test_example(self):
        self.assertTrue(is_rotated_palindrome('121'))
        self.assertTrue(is_rotated_palindrome('112'))
        self.assertTrue(is_rotated_palindrome('211'))

    def test_long(self):
        self.assertTrue(is_rotated_palindrome("risetovotesir"))


if __name__ == '__main__':
    unittest.main()
