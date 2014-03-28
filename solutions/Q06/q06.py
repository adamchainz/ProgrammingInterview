# coding=utf-8


def permutations(string, index=0):
    if index == len(string) - 1:
        return [string]

    results = permutations(string, index + 1)  # With no swapping

    for swap_index in range(index + 1, len(string)):
        swapped_string = (
            string[:index] +
            string[swap_index] +
            string[index + 1:swap_index] +
            string[index] +
            string[swap_index + 1:]
        )
        results.extend(permutations(swapped_string, index + 1))
    return results
