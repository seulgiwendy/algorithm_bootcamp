from collections import deque


def solution(answers):
    match_count = {1: 0, 2: 0, 3: 0}

    first = generate_deque([1, 2, 3, 4, 5])
    second = generate_deque([2, 1, 2, 3, 2, 4, 2, 5])
    third = generate_deque([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])

    for i in range(0, len(answers)):
        answer = answers[i]

        first_choice = first.popleft()
        second_choice = second.popleft()
        third_choice = third.popleft()

        if first_choice == answer:
            match_count[1] = match_count[1] + 1

        if second_choice == answer:
            match_count[2] = match_count[2] + 1

        if third_choice == answer:
            match_count[3] = match_count[3] + 1

        first.append(first_choice)
        second.append(second_choice)
        third.append(third_choice)

    return [key for m in [max(match_count.values())] for key, val in match_count.items() if val == m]


def generate_deque(first_five_choices):
    return deque(first_five_choices)


result = solution([1, 3, 2, 4, 2])
print(result)
