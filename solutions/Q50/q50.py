# coding=utf-8


class CircularListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = self

    def as_list(self):
        values = [self.value]
        current = self.next
        while (current != self):
            values.append(current.value)
            current = current.next
        return values


def insert(head, n):
    if head is None:
        return CircularListNode(n)
    elif head.next == head:
        (head.next, head.next.next) = (CircularListNode(n), head)
        return head.value < n and head or head.next
    elif n < head.value:
        current = head
        while current.next != head:
            current = current.next
        (current.next, current.next.next) = (CircularListNode(n), head)
        return current.next

    current = head
    while current.next != head and current.next.value <= n:
        current = current.next
    (current.next, current.next.next) = (CircularListNode(n), current.next)
    return head
