# coding=utf-8
import unittest
from q04 import parens_sets


class Q04Tests(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(parens_sets(0), set())

    def test_one(self):
        self.assertEqual(parens_sets(1), set(["()"]))

    def test_two(self):
        self.assertEqual(parens_sets(2), set(["()()", "(())"]))

    def test_three(self):
        self.assertEqual(
            parens_sets(3),
            set(["((()))", "(()())", "(())()", "()(())", "()()()"])
        )


if __name__ == '__main__':
    unittest.main()
