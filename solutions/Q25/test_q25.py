# coding=utf-8
import unittest

from q25 import LinkedListNode


class Q25Tests(unittest.TestCase):
    def test_single(self):
        my_list = LinkedListNode.from_list([42])
        self.assertEqual(my_list.midpoint(), 42)

    def test_double(self):
        my_list = LinkedListNode.from_list([1, 3])
        self.assertEqual(my_list.midpoint(), 1)

    def test_triple(self):
        my_list = LinkedListNode.from_list([1, 3, 5])
        self.assertEqual(my_list.midpoint(), 3)

    def test_quadruple(self):
        my_list = LinkedListNode.from_list([1, 3, 5, 7])
        self.assertEqual(my_list.midpoint(), 3)

if __name__ == '__main__':
    unittest.main()
