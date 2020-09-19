from itertools import permutations


def solution(numbers):
    generated_numbers = generate_possible_permutations(numbers)
    generated_numbers.sort()

    return str(generated_numbers[-1])


def generate_possible_permutations(numbers):
    permutation_numbers = permutations(numbers, len(numbers))
    generated_numbers = []

    for number in permutation_numbers:
        generated_numbers.append(int(''.join(map(lambda x: str(x), number))))

    return generated_numbers


print(solution([3, 30, 34, 5, 9]))



