def solution(array):
    answer_count = 0

    for i in range(len(array)):
        if array[i] == 1:
            continue

        check_array = array[i:]
        answer_count += len([j for j in check_array if j == 1])


    return answer_count

print(solution([0, 1, 0, 1, 1]))





