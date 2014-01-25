# coding=utf-8
import unittest

from q44 import preorders_to_inorders


class Q44Tests(unittest.TestCase):
    def test_0_elems(self):
        self.assertEqual(preorders_to_inorders([]), set([tuple()]))

    def test_1_elem(self):
        self.assertEqual(preorders_to_inorders([1]), set([(1,)]))

    def test_2_elems(self):
        self.assertEqual(
            preorders_to_inorders([1, 2]),
            set([
                (1, 2),
                (2, 1)
                ])
        )

    def test_3_elems(self):
        self.assertEqual(
            preorders_to_inorders([1, 2, 3]),
            set([
                (3, 2, 1),
                (2, 3, 1),
                (2, 1, 3),
                (1, 3, 2),
                (1, 2, 3)
                ])
        )

    def test_4_elems(self):
        self.assertEqual(
            preorders_to_inorders(['a', 'd', 'k', 'h']),
            set([
                # All left
                ('h', 'k', 'd', 'a'),
                ('k', 'h', 'd', 'a'),
                ('k', 'd', 'h', 'a'),
                ('d', 'h', 'k', 'a'),
                ('d', 'k', 'h', 'a'),

                # 2-1 split
                ('d', 'k', 'a', 'h'),
                ('k', 'd', 'a', 'h'),

                # 1-2 split
                ('d', 'a', 'k', 'h'),
                ('d', 'a', 'h', 'k'),

                # All right
                ('a', 'h', 'k', 'd'),
                ('a', 'k', 'h', 'd'),
                ('a', 'k', 'd', 'h'),
                ('a', 'd', 'h', 'k'),
                ('a', 'd', 'k', 'h'),
                ])
        )


if __name__ == '__main__':
    unittest.main()
