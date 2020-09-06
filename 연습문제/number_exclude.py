from itertools import combinations


def solution(number, k):
    biggest = 0
    numbers_list = list(number)
    exclude_list = combinations([i for i in range(0, len(numbers_list))], k)



    for exclusions in exclude_list:
        current_numbers = [j for i, j in enumerate(numbers_list) if i not in exclusions]
        generated_number = int("".join(current_numbers))
        if generated_number > biggest:
            biggest = generated_number

    return str(biggest)


print(solution("1924", 2))
print(solution("4177252841", 4))
