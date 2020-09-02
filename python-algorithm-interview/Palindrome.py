# 138 page
def solution(string):
    listified = list(filter(lambda x: x.isalnum(), list(string.lower())))
    for i in range (0, len(listified) // 2):
        if listified[i] != listified[(i + 1) * -1]:
            return False

    return True


print(solution("A man, a plan, a canal: Panama"))
print(solution("race a car"))