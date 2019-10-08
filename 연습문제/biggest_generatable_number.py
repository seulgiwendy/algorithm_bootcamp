from itertools import permutations

def solution(numbers):
    generated_numbers = []

    permutations = generate_possible_permutations(numbers)


def generate_possible_permutations(numbers):
    generated_permutations = []

    permutation_target = []

    for i in range(0, len(numbers)):
        permutation_target.append(i)

    return permutations(permutation_target, len(numbers))


for permu in generate_possible_permutations([1, 2, 3, 4]):
    print(permu)



