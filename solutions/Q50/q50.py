# coding=utf-8


class CircularListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = self


class CircularList(object):
    def __init__(self, values=None):
        self.head = None

        if values is not None:
            for value in values:
                self.insert(value)

    def insert(self, new_value):
        head = self.head
        new = CircularListNode(new_value)

        if self.head is None:  # Zero element list
            self.head = new
        elif new_value < head.value:
            current = head
            while current.next != head:
                current = current.next

            current.next = new
            new.next = head
            self.head = new
        else:
            current = head
            while current.next != head and current.next.value <= new_value:
                current = current.next

            new.next = current.next
            current.next = new

    def values(self):
        values = []

        current = self.head
        while current is not None:
            values.append(current.value)

            current = current.next
            if current is self.head:
                break

        return values

