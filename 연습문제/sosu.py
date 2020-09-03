from math import sqrt
from itertools import permutations, count, islice


def solution(numbers):
    prime_count = 0
    numbers_list = list(numbers)
    generated_permutations = []
    processed_numbers = []

    for i in range(1, len(numbers_list) + 1):
        generated_permutations.append(list(map(''.join, permutations(numbers_list, i))))

    for list_permutation in generated_permutations:
        for i in list_permutation:
            if i.startswith('0'):
                continue
            if i in processed_numbers:
                continue
            if is_prime(int(i)):
                prime_count += 1
            processed_numbers.append(i)

    return prime_count


def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


print(solution("71"))
print(solution("011"))
