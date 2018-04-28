def solution(array):
    array_length = len(array) + 1
    results = []

    for i in range(1, array_length):
        results.append(find_num(array, i))

    return not False in results

def find_num(array, n):
    return n in array


print(solution([1, 2, 3, 5]))