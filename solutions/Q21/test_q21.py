# coding=utf-8
import unittest

from q21 import ContrivedQueue


class Q21Tests(unittest.TestCase):
    def test_simple(self):
        queue = ContrivedQueue()
        queue.enqueue('first')
        queue.enqueue('second')
        queue.enqueue('third')

        self.assertEqual('first', queue.dequeue())
        self.assertEqual('second', queue.dequeue())
        self.assertEqual('third', queue.dequeue())

    def test_interleaved(self):
        queue = ContrivedQueue()
        queue.enqueue('first')
        self.assertEqual('first', queue.dequeue())
        queue.enqueue('second')
        queue.enqueue('third')
        self.assertEqual('second', queue.dequeue())
        self.assertEqual('third', queue.dequeue())

    def test_index_errors(self):
        queue = ContrivedQueue()
        with self.assertRaises(IndexError):
            queue.dequeue()

        queue.enqueue(5)
        queue.dequeue()

        with self.assertRaises(IndexError):
            queue.dequeue()


if __name__ == '__main__':
    unittest.main()
