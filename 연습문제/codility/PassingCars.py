def solution(array):
    answer_count = 0
    zero_pos = 0

    for number in array:
        if number == 0:
            zero_pos += 1

        if number == 1:
            answer_count += zero_pos

    return answer_count

print(solution([0, 1, 0, 1, 1]))





