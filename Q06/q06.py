# coding=utf-8


def permutations(string): 
    results = []
    do_permutations(string, len(string), {}, results)
    return results

def do_permutations(string, string_length, used, results):
    if len(used) == string_length:
        result = ''.join([string[i] for i in used.values()])
        results.append(result)
        return

    for i in range(0, string_length):
        if i not in used.values():
            key = len(used)
            used[key]= i
            do_permutations(string, string_length, used, results)
            del used[key]

    return
