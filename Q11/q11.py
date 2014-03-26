# coding=utf-8


def subsets(elements):
    results = set()
    for i in xrange(2 ** len(elements)):
        binrep = bin(i)[2:]
        result = []
        for i, b in enumerate(reversed(binrep)):
            if b == '1':
                result.append(elements[i])
        results.add(tuple(result))

    return results
