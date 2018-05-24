def solution(decimal):
    numbers = divide(decimal, [])
    divided_numbers = numbers[::-1]

    str_array = []

    for number in divided_numbers:
        if number < 10:
            str_array.append(str(number))
            continue

        if number == 10:
            str_array.append("a")
            continue

        if number == 11:
            str_array.append("b")
            continue

        if number == 12:
            str_array.append("c")
            continue

        if number == 13:
            str_array.append("d")
            continue

        if number == 14:
            str_array.append("e")
            continue

        if number == 15:
            str_array.append("f")
            continue

    return "".join(str_array)


def divide(n, array):

    if n < 16:
        return array + [n]

    new_array = array + [n % 16]
    return divide(n // 16, new_array)

print(solution(1000))