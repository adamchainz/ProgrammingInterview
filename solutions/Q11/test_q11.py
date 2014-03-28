# coding=utf-8
import unittest

from q11 import subsets, subsets_recursive


class Q11TestsMixin(object):
    def test_zero(self):
        self.assertEqual(
            self.check_func([]),
            set([()])
        )

    def test_single(self):
        self.assertEqual(
            self.check_func([1]),
            set([(), (1,)])
        )

    def test_two(self):
        self.assertEqual(
            self.check_func([1, 2]),
            set([(), (1,), (2,), (1, 2)])
        )

    def test_three(self):
        self.assertEqual(
            self.check_func([1, 2, 3]),
            set([(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)])
        )


class Q11NonrecursiveTests(Q11TestsMixin, unittest.TestCase):
    check_func = staticmethod(subsets)


class Q11RecursiveTests(Q11TestsMixin, unittest.TestCase):
    check_func = staticmethod(subsets_recursive)


if __name__ == '__main__':
    unittest.main()
