def solution(d, budget):
    sorted_demand = sorted(d)

    if sum(d) <= budget:
        return len(d)

    return count_sum(sorted_demand, budget)

def count_sum(array, budget):
    possible_count = 0

    for i in range(len(array) + 1):

        if sum(array[0 : i]) == 0:
            continue

        if sum(array[0: i]) <= budget:
            # print("new budget!", array[0 : i])
            possible_count += 1

    return possible_count


print(solution([1, 3, 2, 5, 4], 9))






