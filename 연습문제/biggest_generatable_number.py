from itertools import permutations


def solution(numbers):
    generated_numbers = generate_possible_permutations(numbers)
    joined_numbers = []

    for number in generated_numbers:
        fetched_numbers = ""
        for lower_index in range(0, len(numbers)):
            fetched_numbers += str(number[lower_index])

        joined_numbers.append(int(fetched_numbers))

    joined_numbers.sort()

    return str(joined_numbers[-1]).replace(".0", "")


def generate_possible_permutations(numbers):
    return list(permutations(numbers, len(numbers)))


print(solution([3, 30, 34, 5, 9]))



