# coding=utf-8


def make_change(currency, amount):
    if amount == 0:
        return []

    options = []
    for i, coin in enumerate(currency):
        if coin == amount:
            options.append((coin,))
            break
        elif coin < amount and (amount - coin) >= coin:
            sub_options = make_change(currency[i:], amount - coin)
            for sub_opt in sub_options:
                options.append((coin,) + sub_opt)

    return options
