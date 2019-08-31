def solution(estimates, k):
    sums = {}

    for i in range(0, len(estimates) - k + 1):
        smaller_list = estimates[i:i + k]
        smaller_list_sum = sum(smaller_list)

        sums[smaller_list_sum] = smaller_list

    biggest_key = 0

    for key in sums.keys():
        if key > biggest_key:
            biggest_key = key

    return biggest_key


print solution([1, 1, 9, 3, 7, 6, 5, 10], 4)


