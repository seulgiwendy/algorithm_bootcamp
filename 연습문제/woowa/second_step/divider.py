def solution(integer):
    divider_list = []
    starting_number = integer

    while starting_number > 0:
        if integer % starting_number == 0:
            divider_list.append(starting_number)

        starting_number -= 1

    divider_list.sort()
    str_list = [ str(number) for number in divider_list ]
    return " ".join(str_list)

print(solution(15))
