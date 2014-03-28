# coding=utf-8


def count_in_sorted(item, search):
    """
    Takes an item and an ascendingly sorted list, and returns the number of
    occurences of item in the list
    """
    index = binarysearch(item, search)
    if index is None:
        return 0

    first = index
    for i in range(index, -1, -1):
        if search[i] < item:
            break
        first = i

    last = index
    for i in range(index, len(search)):
        if search[i] > item:
            break
        last = i

    return last - first + 1


def binarysearch(item, search):
    if len(search) == 0:
        return None
    elif len(search) == 1:
        return 0 if search[0] == item else None

    midpoint = len(search) // 2

    if search[midpoint] == item:
        return midpoint
    elif search[midpoint] > item:
        return binarysearch(item, search[:midpoint])
    else:
        subsearch = binarysearch(item, search[midpoint:])
        return None if subsearch is None else midpoint + subsearch
