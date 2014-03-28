# coding=utf-8


def merge_sorted_lists(a, b):
    c = []
    ai = 0
    bi = 0

    while ai < len(a) and bi < len(b):
        if a[ai] <= b[bi]:
            c.append(a[ai])
            ai += 1
        else:
            c.append(b[bi])
            bi += 1

    # Catch any remainders
    c.extend(a[ai:])
    c.extend(b[bi:])

    return c
