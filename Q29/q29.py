# coding=utf-8


def memoize(func):
    results = {}

    def wrapped(n):
        if n not in results:
            results[n] = func(n)
        return results[n]

    return wrapped


@memoize
def staircase_num_ways(n_steps):
    if n_steps <= 1:
        return 1

    total = (
        staircase_num_ways(n_steps - 1) +  # Take 1 step, then same as remainder
        staircase_num_ways(n_steps - 2)  # Take 2 steps, then same as remainder
    )

    # Or, if possible, take 3 steps, then same as remainder
    if total >= 3:
        total += staircase_num_ways(n_steps - 3)

    return total


