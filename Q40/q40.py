# coding=utf-8


class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def inorder_walk(node):
    visited = [node]
    values = []
    while len(visited):
        current = visited.pop()
        if isinstance(current, TreeNode):
            if current.right is not None:
                visited.append(current.right)
            visited.append(current.value)
            if current.left is not None:
                visited.append(current.left)
        else:
            values.append(current)
    return values


def preorder_walk(node):
    visited = [node]
    values = []
    while len(visited):
        current = visited.pop()
        if isinstance(current, TreeNode):
            if current.right is not None:
                visited.append(current.right)
            if current.left is not None:
                visited.append(current.left)
            visited.append(current.value)
        else:
            values.append(current)
    return values
