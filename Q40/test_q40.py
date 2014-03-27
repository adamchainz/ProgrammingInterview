# coding=utf-8
import unittest
from q40 import inorder_walk, preorder_walk, TreeNode


class Q40Tests(unittest.TestCase):
    def test_inorder_single(self):
        tree = TreeNode(4)
        self.assertEqual(inorder_walk(tree), [4])

    def test_inorder_two(self):
        tree = TreeNode(
            4,
            TreeNode(1)
        )
        self.assertEqual(inorder_walk(tree), [1, 4])

    def test_inorder_full(self):
        tree = TreeNode(
            4,
            left=TreeNode(1, right=TreeNode(2)),
            right=TreeNode(7, left=TreeNode(5), right=TreeNode(8))
        )
        self.assertEqual(inorder_walk(tree), [1, 2, 4, 5, 7, 8])

    def test_preorder_single(self):
        tree = TreeNode(4)
        self.assertEqual(preorder_walk(tree), [4])

    def test_preorder_two(self):
        tree = TreeNode(
            4,
            TreeNode(1)
        )
        self.assertEqual(preorder_walk(tree), [4, 1])

    def test_preorder_full(self):
        tree = TreeNode(
            4,
            left=TreeNode(1, right=TreeNode(2)),
            right=TreeNode(7, left=TreeNode(5), right=TreeNode(8))
        )
        self.assertEqual(preorder_walk(tree), [4, 1, 2, 7, 5, 8])


if __name__ == '__main__':
    unittest.main()
