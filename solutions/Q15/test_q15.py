# coding=utf-8
import unittest

from q15 import TreeNode


class Q15Tests(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(TreeNode(5).find_closest(5), 5)
        self.assertEqual(TreeNode(5).find_closest(1), 5)
        self.assertEqual(TreeNode(5).find_closest(10), 5)

    def more_complex(self):
        tree = TreeNode(
            4,
            left=TreeNode(1, right=TreeNode(2)),
            right=TreeNode(7, left=TreeNode(5), right=TreeNode(8))
        )
        self.assertEqual(tree.find_closest(4), 4)
        self.assertEqual(tree.find_closest(2), 2)
        self.assertEqual(tree.find_closest(7), 7)
        self.assertEqual(tree.find_closest(5), 5)
        self.assertEqual(tree.find_closest(8), 8)
        self.assertEqual(tree.find_closest(9), 8)
        self.assertEqual(tree.find_closest(10), 8)
        self.assertEqual(tree.find_closest(0), 1)


if __name__ == '__main__':
    unittest.main()
