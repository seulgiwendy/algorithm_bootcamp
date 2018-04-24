def solution(array):
    current_index = 0
    answer_count = 0

    while(current_index < len(array)):
        if array[current_index] == 1 :
            current_index += 1
            continue

        for i in range(current_index + 1, len(array)):
            if array[i] == 1:
                answer_count += 1

        current_index += 1

    return answer_count




