# coding=utf-8


def all_pairs_summing(sorted_list, m):
    pairs = []
    x = 0
    y = len(sorted_list) - 1
    while x < y:
        total = sorted_list[x] + sorted_list[y]
        if total == m:
            pairs.append((sorted_list[x], sorted_list[y]))
            x += 1
            y -= 1
        elif total < m:
            x += 1
        else:
            y -= 1
    return pairs
