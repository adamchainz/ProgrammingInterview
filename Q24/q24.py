# coding=utf-8


def balance_point(array):
    """
    Return the first point, left-to-right, in a list 'array' s.t. the sum of
    the items on the left is equal to the sum on the right, or None if no such
    point exists.
    """
    total = sum(array)

    if total == 0:
        return None

    left_total = 0
    for i in range(len(array)):
        right_total = total - left_total - array[i]
        if right_total == left_total:
            return i
        left_total += array[i]

    return None
