def solution(array):

    differences = []
    min_diff = 0

    for i in range(1, len(array) - 1):
        iter_array = array[:]
        compare_array = split(iter_array, i)

        differences.append(calculate_difference(compare_array, iter_array))

    min_diff = differences[0]

    for difference in differences:
        if min_diff > difference:
            min_diff = difference

    return min_diff

def split(array, point):
    return_array = array[0:point]
    array[0:point] = []

    return return_array

def calculate_difference(a_array, b_array):
    a_sum = 0
    b_sum = 0

    for a_number in a_array :
        a_sum += a_number

    for b_number in b_array:
        b_sum += b_number

    result = a_sum - b_sum

    if result < 0 :
        return -result

    return result

print(solution([3, 1, 2, 4, 3]))