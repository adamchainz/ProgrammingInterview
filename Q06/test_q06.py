# coding=utf-8
import unittest

from q06 import permutations


class Q6Tests(unittest.TestCase):
    def test_length_one(self):
        self.assertEqual(permutations('1'), ['1'])

    def test_length_two(self):
        self.assertEqual(permutations('12'), ['12', '21'])
        
    def test_length_three(self):
        self.assertEqual(permutations('123'), ['123', '132', '213', '231', '312', '321'])

    def test_length_three_repeated(self):
        self.assertEqual(permutations('111'), ['111', '111', '111', '111', '111', '111'])


if __name__ == '__main__':
    unittest.main()
