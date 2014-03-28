# coding=utf-8


def search_2d_sorted(grid, value):
    y = 0
    x = len(grid[0]) - 1
    while y < len(grid) and x >= 0:
        if grid[y][x] == value:
            return (y, x)
        elif grid[y][x] > value:
            x -= 1
        else:
            y += 1
