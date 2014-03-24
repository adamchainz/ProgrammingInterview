import unittest

from q09 import TreeNode, nodes_at_depth


class Q09Tests(unittest.TestCase):
    def test_single(self):
        tree = TreeNode(5)
        self.assertListEqual(nodes_at_depth(tree, 0), [5])
        self.assertListEqual(nodes_at_depth(tree, 1), [])

    def test_simple(self):
        tree = TreeNode(4, TreeNode(1))
        self.assertListEqual(nodes_at_depth(tree, 0), [4])
        self.assertListEqual(nodes_at_depth(tree, 1), [1])
        self.assertListEqual(nodes_at_depth(tree, 2), [])

    def test_basic(self):
        tree = TreeNode(
            4,
            left=TreeNode(1, right=TreeNode(2)),
            right=TreeNode(7, left=TreeNode(5), right=TreeNode(8))
        )
        self.assertLessEqual(nodes_at_depth(tree, 2), [2, 5, 8])


if __name__ == '__main__':
    unittest.main()
