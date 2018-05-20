cards = {}

cards["A"] = 100
cards["K"] = 90
cards["Q"] = 80
cards["J"] = 70
cards["T"] = 60


def solution(a, b):
    a_array = list(a)
    b_array = list(b)

    a_count = 0
    b_count = 0

    for i in range(0, len(a_array)):

        if return_score(a_array[i]) > return_score(b_array[i]):
            a_count += 1
            continue

        if return_score(b_array[i]) > return_score(a_array[i]):
            b_count += 1
            continue

    return a_count


def return_score(card):
    if ord(card) > 64:
        return cards[card]

    return int(card)


