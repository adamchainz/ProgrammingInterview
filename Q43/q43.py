# coding=utf-8


def decipher_numalpha(string):
    # Base cases
    if len(string) == 0:
        return set([])
    elif string[0] == '0':
        return decipher_numalpha(string[1:])

    # This character will always be useful as part of a recursion
    thischar = numalpha(string[0])
    solutions = set([
        thischar + solution
        for solution in
        decipher_numalpha(string[1:])
    ])

    # Maybe this digit could be part of a two-digit character, in which case,
    # recurse after removing it
    if 1 <= int(string[:2]) <= 26:
        twochars = numalpha(string[:2])
        subsolutions = set([
            twochars + solution
            for solution in
            decipher_numalpha(string[2:])
        ])
        if len(subsolutions):
            solutions.update(subsolutions)
        else:
            solutions.add(twochars)

    return solutions


def numalpha(char):
    num = int(char) - 1
    return chr(num + ord('a'))
