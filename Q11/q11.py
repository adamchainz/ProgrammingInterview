# coding=utf-8


def subsets(elements):
    results = set()
    for i in range(2 ** len(elements)):
        binrep = bin(i)[2:]
        result = []
        for i, b in enumerate(reversed(binrep)):
            if b == '1':
                result.append(elements[i])
        results.add(tuple(result))

    return results


def subsets_recursive(elements):
    if len(elements) == 0:
        return set([()])

    this, others = elements[0], elements[1:]
    results = set()
    sub_results = subsets_recursive(others)

    # All possible subsets = all possible subsets of 'others',
    # without or with 'this' element
    results.update(sub_results)
    for sub_result in sub_results:
        results.add((this,) + sub_result)

    return results
