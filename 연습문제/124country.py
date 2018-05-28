numbers = ["4", "1", "2"]


def solution(n):
    answer = ""
    while n > 0:
        n, a = divmod(n, 3)

        if a == 0:
            n -= 1
        answer = numbers[a] + answer

    return answer

print(solution(12))

