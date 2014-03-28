# coding=utf-8


def is_rotated_palindrome(string):
    if len(string) <= 1:
        return True

    index = lambda n: (n + len(string)) % len(string)

    for i in range(len(string)):
        for j in range(1, (len(string) // 2) + 1):
            if string[index(i + j)] != string[index(i - j)]:
                break
            return True

    return False
