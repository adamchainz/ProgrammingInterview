# coding=utf-8


class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def find_closest(self, m):
        closest = self.value

        if m < self.value and self.left is not None:
            closest_left = self.left.find_closest(m)
            if abs(m - closest_left) < abs(m - self.value):
                closest = closest_left
        elif m > self.value and self.right is not None:
            closest_right = self.right.find_closest(m)
            if abs(m - closest_right) < abs(m - self.value):
                closest = closest_right

        return closest
