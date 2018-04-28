def solution(string):
    current_index = 0
    str_list = list(string)
    results = []

    while current_index < len(str_list):
        for i in range(current_index, len(str_list)):
            if(is_palindrome(str_list[current_index : i + 1])):
                results.append(len(str_list[current_index : i + 1]))

        current_index += 1

    if len(results) > 0:
        return max(results)

    return 0



def is_palindrome(string):
    str_list = string
    if len(str_list) < 3:
        return False

    for i in range(len(str_list) // 2):
        if str_list[i] == str_list[-(i + 1)]:
            continue
        else:
            return False
    return True

print(solution('abacde'))