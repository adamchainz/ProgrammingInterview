# coding=utf-8
import unittest

from q27 import LinkedList


class Q27Tests(unittest.TestCase):
    def test_no_rotation(self):
        my_list = LinkedList([1, 2, 3, 4])
        my_list.rotate(0)
        self.assertEqual(my_list.to_list(), [1, 2, 3, 4])

    def test_one(self):
        my_list = LinkedList([1, 2, 3, 4])
        my_list.rotate(1)
        self.assertEqual(my_list.to_list(), [2, 3, 4, 1])

    def test_two(self):
        my_list = LinkedList([1, 2, 3, 4])
        my_list.rotate(2)
        self.assertEqual(my_list.to_list(), [3, 4, 1, 2])

    def test_three(self):
        my_list = LinkedList([1, 2, 3, 4])
        my_list.rotate(3)
        self.assertEqual(my_list.to_list(), [4, 1, 2, 3])

    def test_whole(self):
        my_list = LinkedList([1, 2, 3, 4])
        my_list.rotate(4)
        self.assertEqual(my_list.to_list(), [1, 2, 3, 4])

    def test_too_much(self):
        my_list = LinkedList([1, 2, 3, 4])
        with self.assertRaises(ValueError):
            my_list.rotate(5)

        with self.assertRaises(ValueError):
            my_list.rotate(999)

    def test_negative(self):
        my_list = LinkedList([1, 2, 3, 4])
        with self.assertRaises(ValueError):
            my_list.rotate(-1)


if __name__ == '__main__':
    unittest.main()
