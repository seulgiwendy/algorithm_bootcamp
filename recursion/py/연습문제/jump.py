def jumpCase(num):
    answer = find_cases(num)

    return answer

def find_cases(num):

    if num == 1:
        return 1

    if num == 2:
        return 2

    return find_cases(num - 1) + find_cases(num - 2)

print(jumpCase(13))