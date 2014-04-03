# coding=utf-8


def reverse(listy):
    """
    We're using lists because Python's strings are immutable and therefore
    don't work the same way as in the video.
    """
    for i in range(len(listy) // 2):
        i2 = len(listy) - i - 1
        listy[i], listy[i2] = listy[i2], listy[i]
