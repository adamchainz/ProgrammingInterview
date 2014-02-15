import unittest
from q42 import subsets


class SubsetsTests(unittest.TestCase):
    def test_zero(self):
        self.assertSetEqual(
            subsets([1], 0),
            set()
        )

    def test_single(self):
        self.assertSetEqual(
            subsets([1], 1),
            set([(1,)])
        )

    def test_two(self):
        self.assertSetEqual(
            subsets([1, 2, 3], 2),
            set([(1, 2), (1, 3), (2, 3)])
        )

    def test_three(self):
        self.assertSetEqual(
            subsets([1, 2, 3], 3),
            set([(1, 2, 3)])
        )

if __name__ == '__main__':
    unittest.main()
