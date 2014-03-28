# coding=utf-8
import unittest

from q19 import spiralize


class Q19Tests(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(spiralize([[42]]), [42])

    def test_2x2(self):
        grid = [
            [1, 4],
            [3, 9]
        ]
        self.assertEqual(spiralize(grid), [1, 4, 9, 3])

    def test_3x3(self):
        grid = [
            [77, 66, 44],
            [17, 16, 14],
            [37, 36, 34],
        ]
        self.assertEqual(
            spiralize(grid),
            [77, 66, 44, 14, 34, 36, 37, 17, 16]
        )

    def test_4x4(self):
        grid = [
            [5, 4, 3, 2],
            [9, 8, 7, 3],
            [5, 1, 3, 4],
            [1, 0, 0, 5],
        ]
        self.assertEqual(
            spiralize(grid),
            [5, 4, 3, 2, 3, 4, 5, 0, 0, 1, 5, 9, 8, 7, 3, 1]
        )

if __name__ == '__main__':
    unittest.main()
