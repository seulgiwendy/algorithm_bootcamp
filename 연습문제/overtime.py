import math

def overtime(n, works):
    if n >= sum(works):
        return 0

    while n > 0:
        max_value = max(works)
        max_index = works.index(max_value)

        works[max_index] -= 1
        n -= 1

    return calculate_overtime_index(works)

def calculate_overtime_index(works):
    powered_sum = 0

    for work in works:
        powered_sum += math.pow(work, 2)

    return powered_sum


