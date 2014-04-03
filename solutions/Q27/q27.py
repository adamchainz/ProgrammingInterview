# coding=utf-8


class LinkedList(object):
    class Node(object):
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def __init__(self, listy):
        self.head = None
        prev = None
        for val in listy:
            node = self.Node(val)
            if prev:
                prev.next = node
            if self.head is None:
                self.head = node
            prev = node

    def to_list(self):
        listy = []
        node = self.head
        while node is not None:
            listy.append(node.val)
            node = node.next
        return listy

    def rotate(self, n):
        if n < 0:
            raise ValueError("Can only rotate in one direction")
        elif n == 0:
            return

        start = self.head
        end = self.head
        while n:
            if end is None:
                raise ValueError("Tried to rotate LinkedList more than its length")
            end_prev = end
            end = end.next
            n -= 1

        if end is None:  # n = length of list
            return

        self.last_node.next = start
        self.head = end
        end_prev.next = None

    @property
    def last_node(self):
        node = self.head
        while node.next is not None:
            node = node.next
        return node
