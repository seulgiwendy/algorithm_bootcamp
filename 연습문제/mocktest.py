import collections


def solution(answers):
    match_count = {
        1: make_choice(collections.deque([1, 2, 3, 4, 5]), answers),
        2: make_choice(collections.deque([2, 1, 2, 3, 2, 4, 2, 5]), answers),
        3: make_choice(collections.deque([3, 3, 1, 1, 2, 2, 4, 4, 5, 5]), answers)}

    biggest_count = [1]

    for match_number in match_count:

        if match_count[biggest_count[0]] < match_count[match_number]:
            biggest_count[0] = match_number
            continue

        if match_count[biggest_count[0]] == match_count[match_number]:
            biggest_count.append(match_number)
            continue

    returnable_list = list(set(biggest_count))
    returnable_list.sort()

    return returnable_list


def make_choice(choices, answers):
    match_count = 0

    for answer in answers:
        if choices[0] == answer:
            match_count += 1
        choices.rotate(-1)

    return match_count


print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))