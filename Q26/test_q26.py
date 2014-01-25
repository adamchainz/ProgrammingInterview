# coding=utf-8
import unittest

from q26 import is_palindrome, longest_palindrome


class Q26Tests(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(''))
        self.assertTrue(is_palindrome('a'))
        self.assertTrue(is_palindrome('aa'))
        self.assertTrue(is_palindrome('aba'))
        self.assertFalse(is_palindrome('ab'))
        self.assertFalse(is_palindrome('abc'))

    def test_base0(self):
        self.assertEqual(longest_palindrome(''), '')

    def test_base1(self):
        self.assertEqual(longest_palindrome('1'), '1')

    def test_all_even(self):
        self.assertEqual(longest_palindrome('aa'), 'aa')

    def test_all_odd(self):
        self.assertEqual(longest_palindrome('aba'), 'aba')

    def test_example(self):
        self.assertEqual(longest_palindrome('4123215'), '12321')

if __name__ == '__main__':
    unittest.main()
