def digit_reverse(n):
    string_num = str(n)
    str_list = list(string_num)
    answer_list = []

    while len(str_list) > 0 :
        answer_list.append(int(str_list.pop()))

    return answer_list


print(digit_reverse(54321))

