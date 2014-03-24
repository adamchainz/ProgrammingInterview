# coding=utf-8
from fractions import gcd


def to_rational(double):
    denominator = 1
    while (double * denominator % 1) != 0:
        denominator *= 10

    numerator = double * denominator
    d = gcd(numerator, denominator)
    return "%d/%d" % (numerator/d, denominator/d)
