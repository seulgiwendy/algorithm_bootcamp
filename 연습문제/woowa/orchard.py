import itertools


def solution(a, k, l):

    if len(a) < k + l:
        return -1

    first_sums = create_sublist(a, k)
    print(first_sums)

    second_sums = create_sublist(a, l)
    print(second_sums)

    return max(first_sums) + max(second_sums)



def create_sublist(array, length):

    starting_point = 0
    sums = []

    while(starting_point < len(array)):
        sublist = []
        sublist.append(array[starting_point])

        for i in range(starting_point + 1, length + starting_point):
            if i == len(array) or i >= len(array):
                continue
            sublist.append(array[i])

        if len(sublist) < length:
            starting_point += 1
            continue

        sums.append(sum(sublist))


        starting_point += 1

    return sums

print(solution([6, 1, 4, 6, 3, 2, 7, 4], 3, 2))


