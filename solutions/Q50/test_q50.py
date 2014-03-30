# coding=utf-8
import unittest

from q50 import CircularListNode, insert


class Q50Tests(unittest.TestCase):
    def test_first(self):
        head = insert(None, 1)
        self.assertEqual(head.as_list(), [1])

    def test_second(self):
        head = CircularListNode(1)
        head = insert(head, 2)
        self.assertEqual(head.as_list(), [1, 2])

    def test_head(self):
        head = CircularListNode(2)
        head.next = CircularListNode(3)
        head.next.next = head
        head = insert(head, 1)
        self.assertEqual(head.as_list(), [1, 2, 3])

    def test_middle(self):
        head = CircularListNode(1)
        head.next = CircularListNode(3)
        head.next.next = head
        head = insert(head, 2)
        self.assertEqual(head.as_list(), [1, 2, 3])

    def test_tail(self):
        head = CircularListNode(1)
        head.next = CircularListNode(2)
        head.next.next = head
        head = insert(head, 3)
        self.assertEqual(head.as_list(), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
