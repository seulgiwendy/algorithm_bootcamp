import math

def binary(decimal, array):
    if decimal < 1:
        return array[::-1]
    array.append(decimal % 2)
    return binary(decimal // 2, array)


def decimal(binary):
    binary_digits = list(binary)[::-1]

    result = 0

    for i in range(len(binary_digits)):
        result += (int(binary_digits[i]) *  math.pow(2, i))

    return int(result)

print(binary(15, []))
print(decimal("111"))

