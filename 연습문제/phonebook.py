def solution(phone_book):
    prefix_hash = {}
    listified_numbers = []

    for number in phone_book:
        if number in prefix_hash:
            return False
        prefix_hash[number] = 1
        listified_numbers.append(listify_number(number))

    for numbers_list in listified_numbers:
        for number in numbers_list:
            if number in prefix_hash:
                prefix_hash[number] += 1

    for prefixes in prefix_hash:
        if prefix_hash[prefixes] > 2:
            return False

    return True


def listify_number(number):
    listified_number = []
    splitted_number = list(number)

    for j in range(1, len(splitted_number) + 1):
        listified_number.append(''.join(splitted_number[0:j]))

    return listified_number


print(solution(["12", "123", "1235", "567", "88"]))
print(solution(["123", "456", "789"]))
