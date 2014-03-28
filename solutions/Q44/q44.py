# coding=utf-8


def preorders_to_inorders(preorders):
    # For convenience, empty array has 1 solution, the empty tuple
    if len(preorders) == 0:
        return set([tuple()])

    front, back = preorders[0], preorders[1:]

    solutions = set()

    for i in range(len(back) + 1):
        left, right = back[:i], back[i:]

        for left_solution in preorders_to_inorders(left):
            for right_solution in preorders_to_inorders(right):
                solutions.add(left_solution + (front,) + right_solution)

    return solutions
