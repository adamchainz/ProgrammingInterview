# coding=utf-8


def maximal_submatrix_sum(matrix):
    width = len(matrix)
    height = len(matrix[0])

    @memoize
    def matrix_sum(i, j, w, h):
        if w > 1:
            the_sum = matrix_sum(i, j, w - 1, h)
            # Add on final column
            for y in range(j, j + h):
                the_sum += matrix[i + w - 1][y]
            return the_sum
        elif h > 1:
            the_sum = matrix_sum(i, j, w, h - 1)
            # Add on final row
            for x in range(i, i + w):
                the_sum += matrix[x][j + h - 1]
            return the_sum
        else:
            return matrix[i][j]

    max_sum = float('-inf')
    for w in range(1, width + 1):
        for h in range(1, height + 1):
            for i in range(width - w + 1):
                for j in range(height - h + 1):
                    # Check for sum of matrix width w, height h, at pos i,j
                    sum_here = matrix_sum(i, j, w, h)
                    if sum_here > max_sum:
                        max_sum = sum_here

    return max_sum


def memoize(func):
    results = {}

    def wrapped(*args):
        key = tuple(args)
        if key not in results:
            results[key] = func(*args)
        return results[key]

    return wrapped
