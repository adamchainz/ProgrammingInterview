# coding=utf-8


def first_index(numbers, value, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(numbers) - 1

    if value < numbers[start] or value > numbers[end]:
        return None

    midpoint = (start + end) / 2
    if numbers[midpoint] > value or (midpoint - 1 >= 0 and
                                     numbers[midpoint - 1] == value):
        return first_index(numbers, value, start, midpoint - 1)
    elif numbers[midpoint] < value:
        return first_index(numbers, value, midpoint + 1, end)
    else:
        return midpoint
