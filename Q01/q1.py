# coding=utf-8


class LinkedListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def to_list(self):
        if self.next is not None:
            return [self.val] + self.next.to_list()
        else:
            return [self.val]

    @classmethod
    def from_list(cls, listy):
        first = None
        prev = None
        for val in listy:
            node = LinkedListNode(val)
            if prev:
                prev.next = node
            if first is None:
                first = node
            prev = node

        return first

    def reverse(self):
        stack = []
        node = self
        while node is not None:
            stack.append(node.val)
            node = node.next

        first = None
        prev = None
        while len(stack):
            newnode = LinkedListNode(stack.pop())
            if prev:
                prev.next = newnode
            if first is None:
                first = newnode
            prev = newnode

        return first
