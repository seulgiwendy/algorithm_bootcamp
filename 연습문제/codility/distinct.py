def solution(array):
    if len(array) == 0:
        return 0

    count = 1
    array.sort()

    for i in range(len(array) - 1):
        if array[i] != array[i + 1]:
            count += 1

    return count

print(solution([2, 1, 1, 2, 3, 1]))