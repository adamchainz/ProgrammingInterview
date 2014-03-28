# coding=utf-8


def num_rotations_til_sorted(array):
    i = 1
    while i < len(array):
        if array[i - 1] > array[i]:
            return min(i, len(array) - i)
        i += 1
    return 0
