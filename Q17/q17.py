# coding=utf-8


def my_division(numerator, denominator):
    if denominator == 0:
        raise ZeroDivisionError()

    divisor = denominator
    divisor_size = 1
    count = 0
    while numerator >= denominator:
        if numerator >= divisor:
            numerator -= divisor
            count += divisor_size
            # Double divisor
            divisor <<= 1
            divisor_size <<= 1
        elif numerator < divisor:
            # Halve divisor
            divisor >>= 1
            divisor_size >>= 1

    return count
