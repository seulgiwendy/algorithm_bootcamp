def solution(array, k):

    new_array = []

    for i in range(len(array)):
        new_index = i + k
        if new_index > len(array) - 1:
            new_array.insert(new_index % len(array), array[i])
            continue

        new_array.insert(new_index, array[i])

    return new_array

print(solution([3, 8, 9, 7, 6], 3))
