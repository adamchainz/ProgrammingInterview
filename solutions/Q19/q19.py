# coding=utf-8


def spiralize(grid):
    """
    Takes a list of lists in y, x order, and outputs a clockwise spiral
    linearisation of those values
    """
    out = []

    height = len(grid)
    width = len(grid[0])

    x = -1
    y = 0
    i = 0
    while True:
        if (i % 2) == 0:
            side_length = width - (i // 2)
        else:
            side_length = height - (i // 2) - 1

        if side_length == 0:
            return out

        y_inc, x_inc = _increments(i)

        for _ in range(side_length):
            y += y_inc
            x += x_inc
            out.append(grid[y][x])

        i += 1


def _increments(i):
    im = i % 4
    if im == 0:
        return 0, 1
    elif im == 1:
        return 1, 0
    elif im == 2:
        return 0, -1
    elif im == 3:
        return -1, 0
