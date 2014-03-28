# coding=utf-8


def max_consecutive_sum(array):
    if len(array) == 0:
        return 0

    start = 0
    end = 0
    total = 0
    best_found = float('-inf')
    while end < len(array):
        total += array[end]
        while start < end and array[start] < 0:
            total -= array[start]
            start += 1
        best_found = max(total, best_found)
        end += 1
    return best_found
