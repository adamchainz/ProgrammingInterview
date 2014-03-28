# coding=utf-8
import unittest

from q29 import staircase_num_ways


class Q29Tests(unittest.TestCase):
    def test_one(self):
        self.assertEqual(staircase_num_ways(1), 1)

    def test_two(self):
        self.assertEqual(staircase_num_ways(2), 2)

    def test_three(self):
        self.assertEqual(staircase_num_ways(3), 4)

    def test_four(self):
        self.assertEqual(staircase_num_ways(4), 7)

    def test_five(self):
        self.assertEqual(staircase_num_ways(5), 13)

if __name__ == '__main__':
    unittest.main()
