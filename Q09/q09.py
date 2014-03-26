# coding=utf-8


class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def nodes_at_depth(tree, depth):
    if depth == 0:
        return [tree.value]

    results = []
    if tree.left is not None:
        results.extend(nodes_at_depth(tree.left, depth - 1))
    if tree.right is not None:
        results.extend(nodes_at_depth(tree.right, depth - 1))
    return results
