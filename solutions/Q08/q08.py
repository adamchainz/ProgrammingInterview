# coding=utf-8


class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validate_is_search_tree(node):
    is_valid = True

    if node.left is not None:
        is_valid &= (
            node.value >= node.left.value and
            validate_is_search_tree(node.left)
        )

    if node.right is not None:
        is_valid &= (
            node.value < node.right.value and
            validate_is_search_tree(node.right)
        )

    return is_valid
