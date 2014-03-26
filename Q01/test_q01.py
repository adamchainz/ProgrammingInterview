# coding=utf-8
import unittest

from q01 import LinkedListNode


class Q01Tests(unittest.TestCase):
    def test_example(self):
        self.assertListEqual(
            LinkedListNode.from_list([1, 2, 3]).reverse().to_list(),
            [3, 2, 1]
        )

    def test_example_longer(self):
        self.assertListEqual(
            LinkedListNode.from_list([1, 2, 3, 7, 9]).reverse().to_list(),
            [9, 7, 3, 2, 1]
        )

if __name__ == '__main__':
    unittest.main()
