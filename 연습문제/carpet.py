def solution(brown, yellow):
    sum = brown + yellow
    dividers = []

    for i in range(1, sum):
        if i in dividers:
            continue

        if sum % i == 0:
            dividers.append(i)

    print(dividers)
    answer = []

    selected_divider = dividers[len(dividers) // 2]
    answer.append(selected_divider)
    answer.append(sum // selected_divider)

    return sorted(answer)[::-1]


print(solution(22, 2))