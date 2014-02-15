import unittest
from q40 import inorder_walk, preorder_walk, TreeNode


class InorderWalkTests(unittest.TestCase):
    def test_single(self):
        tree = TreeNode(4)
        self.assertListEqual(inorder_walk(tree), [4])

    def test_two(self):
        tree = TreeNode(
            4,
            TreeNode(1)
        )
        self.assertListEqual(inorder_walk(tree), [1, 4])

    def test_full(self):
        tree = TreeNode(
            4,
            left=TreeNode(1, right=TreeNode(2)),
            right=TreeNode(7, left=TreeNode(5), right=TreeNode(8))
        )
        self.assertListEqual(inorder_walk(tree), [1, 2, 4, 5, 7, 8])


class PreorderWalkTests(unittest.TestCase):
    def test_single(self):
        tree = TreeNode(4)
        self.assertListEqual(preorder_walk(tree), [4])

    def test_two(self):
        tree = TreeNode(
            4,
            TreeNode(1)
        )
        self.assertListEqual(preorder_walk(tree), [4, 1])

    def test_full(self):
        tree = TreeNode(
            4,
            left=TreeNode(1, right=TreeNode(2)),
            right=TreeNode(7, left=TreeNode(5), right=TreeNode(8))
        )
        self.assertListEqual(preorder_walk(tree), [4, 1, 2, 7, 5, 8])


if __name__ == '__main__':
    unittest.main()
