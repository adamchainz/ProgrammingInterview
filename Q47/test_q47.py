# coding=utf-8
import unittest

from q47 import TreeNode


class Q47Tests(unittest.TestCase):
    def test_root_only(self):
        node = TreeNode(77)
        self.assertListEqual(node.postorder_traversal(), [77])

    def test_example(self):
        root = TreeNode(
            4,
            left=TreeNode('a'),
            right=TreeNode(
                7,
                left=TreeNode(2)
            )
        )
        self.assertListEqual(
            root.postorder_traversal(),
            ['a', 2, 7, 4]
        )

    def test_big(self):
        root = TreeNode(
            9,
            left=TreeNode(
                8,
                left=TreeNode(4),
                right=TreeNode(2)
            ),
            right=TreeNode(
                7,
                left=TreeNode(6),
                right=TreeNode(5)
            )
        )
        self.assertListEqual(
            root.postorder_traversal(),
            [4, 2, 8, 6, 5, 7, 9]
        )


if __name__ == '__main__':
    unittest.main()
