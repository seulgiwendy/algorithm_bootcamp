def nextBigNumber(n):
    one_count = count_one(convert_to_binary(n, []))
    print(one_count)

    start_index = n + 1

    while(start_index > n):
        if count_one(convert_to_binary(start_index, [])) == one_count:
            return start_index
        start_index += 1

    return 0

def convert_to_binary(n, digits):

    if n == 0:
        return digits[::-1]

    digits.append(n % 2)

    return convert_to_binary(n // 2, digits)

def convert_to_decimal(binary_digits):

    converted_number = 0

    for i in range(0, len(binary_digits)):
        converted_number += binary_digits[i] * pow(2, i)

    return converted_number

def count_one(digits):

    count = 0

    for digit in digits:
        if digit == 1:
            count += 1

    return count

def pow(n, power):

    if power == 0:
        return 1

    if power == 1:
        return n

    return n * pow(n, power - 1)

print(nextBigNumber(16))