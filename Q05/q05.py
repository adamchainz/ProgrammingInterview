# coding=utf-8


def to_rational(double):
    denominator = 1
    while double*denominator % 1 != 0:
        denominator *= 10

    numerator = double * denominator
    d = greatest_common_divisor(numerator, denominator)
    return "%d/%d" % (numerator/d, denominator/d)


def greatest_common_divisor(a, b):
    """
    Finds the greatest common divisor of two numbers using the Euclidean
    Algorithm.
    """
    while b != 0:
        t = b
        b = a % b
        a = t

    return a
