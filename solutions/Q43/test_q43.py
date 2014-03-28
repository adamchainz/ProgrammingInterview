# coding=utf-8
import unittest

from q43 import decipher_numalpha, numalpha


class Q43Tests(unittest.TestCase):
    def test_numalpha(self):
        self.assertEqual(numalpha('1'), 'a')
        self.assertEqual(numalpha('26'), 'z')

    def test_base0(self):
        self.assertEqual(decipher_numalpha(''), set([]))

    def test_base1(self):
        self.assertEqual(decipher_numalpha('1'), set(['a']))
        self.assertEqual(decipher_numalpha('9'), set(['i']))

    def test_simple_recursion(self):
        self.assertEqual(decipher_numalpha('12'), set(['ab', 'l']))

    def test_example(self):
        self.assertEqual(decipher_numalpha('123'), set(['abc', 'lc', 'aw']))

    def test_handle_0s(self):
        self.assertEqual(decipher_numalpha('10'), set(['j']))

    def test_over_20(self):
        self.assertEqual(decipher_numalpha('29'), set(['bi']))


if __name__ == '__main__':
    unittest.main()
