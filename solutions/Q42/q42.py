# coding=utf-8


def subsets(elements, k):
    results = set()
    for i in range(2 ** len(elements)):
        binrep = bin(i)[2:]
        if k and binrep.count('1') == k:
            result = []
            for i, b in enumerate(reversed(binrep)):
                if b == '1':
                    result.append(elements[i])
            results.add(tuple(result))

    return results
