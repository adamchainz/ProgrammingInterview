# coding=utf-8


def first_index(numbers, value, start, end):
    if end < start or value < numbers[start] or value > numbers[end]:
        return -1
    else:
        midpoint = (start + end) / 2
        if numbers[midpoint] > value or (midpoint-1 >= 0 and 
                                         numbers[midpoint-1] == value):
            return first_index(numbers, value, start, midpoint-1)
        elif numbers[midpoint] < value:
            return first_index(numbers, value, midpoint+1, end)
        else:
            return midpoint
