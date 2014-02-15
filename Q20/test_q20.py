import unittest
from q20 import search_2d_sorted


class Search2DSortedTests(unittest.TestCase):
    def test_simple_there(self):
        self.assertEqual(
            search_2d_sorted([[1]], 1),
            (0, 0)
        )

    def test_simple_missing(self):
        self.assertEqual(
            search_2d_sorted([[2]], 1),
            None
        )

    def test_example(self):
        grid = [
            [1, 4, 5],
            [2, 6, 7],
            [3, 8, 9]
        ]
        self.assertEqual(
            search_2d_sorted(grid, 4),
            (0, 1)
        )


if __name__ == '__main__':
    unittest.main()
