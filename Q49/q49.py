# coding=utf-8


def longest_increasing_subs(array):
    if len(array) <= 1:
        return array

    subsolution = longest_increasing_subs(array[1:])
    if array[0] < subsolution[0]:
        return [array[0]] + subsolution
    else:
        at_here = increasing_subs(array)
        if len(at_here) >= len(subsolution):
            return at_here
        else:
            return subsolution


def increasing_subs(array):
    end = 0
    for i in xrange(1, len(array)):
        if array[i] > array[i - 1]:
            end = i
        else:
            break
    return array[:(end + 1)]

