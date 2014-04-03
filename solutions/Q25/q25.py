# coding=utf-8
import itertools


class LinkedListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

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

    def midpoint(self):
        head = self
        head2 = self

        for i in itertools.count():
            head2 = head2.next
            if head2 is None:
                break
            elif i % 2 == 1:
                head = head.next

        return head.val
