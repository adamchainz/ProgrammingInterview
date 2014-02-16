

def parens_sets(n):
    if n == 0:
        return set()
    elif n == 1:
        return set(["()"])

    found = set()
    for paren_string in parens_sets(n - 1):
        found.add("()" + paren_string)
        found.add(paren_string + "()")
        found.add("(" + paren_string + ")")

    return found
