# coding=utf-8


class TreeNode(object):
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def postorder_traversal(self):
        output = []

        examine = self
        stack = [self]
        while len(stack):
            examine = stack.pop()
            if examine.left:
                stack.append(examine.left)
            if examine.right:
                stack.append(examine.right)

            output.append(examine.key)

        output.reverse()

        return output
