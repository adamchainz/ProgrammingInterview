# coding=utf-8
import unittest
from q08 import TreeNode, validate_is_search_tree


class Q08Tests(unittest.TestCase):
    def test_simple_yes(self):
        self.assertTrue(validate_is_search_tree(
            TreeNode(5)
        ))

    def test_simple_no(self):
        self.assertTrue(validate_is_search_tree(
            TreeNode(
                5,
                left=TreeNode(8)
            )
        ))

    def test_bigger_yes(self):
        self.assertTrue(validate_is_search_tree(
            TreeNode(
                3,
                left=TreeNode(2, left=TreeNode(1)),
                right=TreeNode(5, left=TreeNode(4), right=TreeNode(6))
            )
        ))


if __name__ == '__main__':
    unittest.main()
