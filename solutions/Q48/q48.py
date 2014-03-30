# coding=utf-8


def max_subsequent_product(numbers):
    """
    Assumes that the given list has a subsequence with product greater than 1
    """
    max = 1
    curr_pos = 1
    curr_neg = 1
    for number in numbers:
        if number > 0:
            curr_pos *= number
            if curr_neg < 0:
                curr_neg *= number
        elif number < 0:
            if curr_neg < 0:
                (curr_pos, curr_neg) = (curr_neg * number, curr_pos * number)
            else:
                curr_neg = curr_pos * number
                curr_pos = 1
        else:
            curr_pos = 1
            curr_neg = 1

        if curr_pos > max:
            max = curr_pos

    return max
