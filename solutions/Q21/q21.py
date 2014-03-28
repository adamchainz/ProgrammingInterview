# coding=utf-8


class ContrivedQueue(object):
    def __init__(self):
        # There are no stacks in native Python, so we'll use lists; however in
        # Python 3, you can remove from both ends of a list in O(1), but let's
        # just pretend they're stacks.
        self._head = []
        self._tail = []
        self._which = 'a'

    def enqueue(self, val):
        self._tail.append(val)

    def dequeue(self):
        if not len(self._head):
            while len(self._tail):
                self._head.append(self._tail.pop())

        if not len(self._head):
            raise IndexError("dequeue from empty ContrivedQueue")

        return self._head.pop()

