def solution(x, y, d):
    multiplier = (y - x) // d

    if multiplier * d + x < y:
        return multiplier + 1

    return multiplier



print(solution(10, 85, 30))