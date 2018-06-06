def solution(n):
    binary_array = to_binary(n)
    lengths = count_zero(binary_array)

    if len(lengths) == 0:
        return 0

    return max(lengths)

def to_binary(n):
    div_array = []
    number = n

    while number > 0:
        div_array.append(number % 2)
        number = number // 2

    return div_array[::-1]

def count_zero(array):
    counts = []
    start_index = -1

    for i in range(len(array)):
        if array[i] == 1:
            if start_index != -1:
                counts.append(i - start_index - 1)
                start_index = i
                continue
            start_index = i

    return counts

print(solution(1041))

