# coding=utf-8


def max_rect(histogram):
    rect_stack = []
    max_found = float('-inf')

    for i in range(len(histogram) + 1):
        while len(rect_stack):
            if i < len(histogram) and histogram[i] >= rect_stack[-1][1]:
                break

            start, size = rect_stack.pop()
            area = (i - start) * size
            max_found = max(max_found, area)

        if i < len(histogram):
            rect_stack.append((i, histogram[i]))

    return max_found
