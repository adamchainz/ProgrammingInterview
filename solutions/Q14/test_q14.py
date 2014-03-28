# coding=utf-8
import unittest

from q14 import make_change


class Q14Tests(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(make_change([1], 1), [(1,)])
        self.assertEqual(make_change([33], 33), [(33,)])

    def test_multiples(self):
        self.assertEqual(make_change([1], 6), [(1,) * 6])
        self.assertEqual(make_change([2], 6), [(2,) * 3])
        self.assertEqual(make_change([3], 6), [(3,) * 2])
        self.assertEqual(make_change([5], 6), [])

    def test_double(self):
        self.assertEqual(
            make_change([1, 2], 1),
            [(1,)]
        )
        self.assertEqual(
            make_change([1, 2], 2),
            [(1, 1,), (2,)]
        )
        self.assertEqual(
            make_change([1, 2], 3),
            [(1, 1, 1,), (1, 2,)]
        )
        self.assertEqual(
            make_change([1, 2], 4),
            [(1, 1, 1, 1), (1, 1, 2), (2, 2,)]
        )

    def test_larger(self):
        self.assertEqual(
            make_change([1, 2, 5], 7),
            [(1, 1, 1, 1, 1, 1, 1,),
             (1, 1, 1, 1, 1, 2,),
             (1, 1, 1, 2, 2,),
             (1, 1, 5,),
             (1, 2, 2, 2,),
             (2, 5,)]
        )

if __name__ == '__main__':
    unittest.main()
