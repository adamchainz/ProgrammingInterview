# coding=utf-8
import unittest

from q50 import CircularList


class Q50Tests(unittest.TestCase):
    def test_insert_smaller(self):
        clist = CircularList([2])
        clist.insert(1)
        self.assertEqual(clist.values(), [1, 2])

    def test_insert_bigger(self):
        clist = CircularList([1])
        clist.insert(2)
        self.assertEqual(clist.values(), [1, 2])

    def test_insert_equal(self):
        clist = CircularList([1])
        clist.insert(1)
        self.assertEqual(clist.values(), [1, 1])

    def test_insert_middle(self):
        clist = CircularList([1, 3])
        clist.insert(2)
        self.assertEqual(clist.values(), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
