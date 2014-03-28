# coding=utf-8
import math


def longest_palindrome(string):
    longest = ''
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substr = string[i:j]
            if (j - i) >= len(longest) and is_palindrome(substr):
                longest = substr

    return longest


def is_palindrome(string):
    midpoint = int(math.ceil(len(string) / 2.0))
    for i in range(midpoint):
        if string[i] != string[len(string) - i - 1]:
            return False

    return True
