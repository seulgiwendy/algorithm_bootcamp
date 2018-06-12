def bubble(list):
    current_index = 0
    while current_index < len(list) - 1:
        for i in range(current_index, len(list) - 1):
            temp = 0
            if list[i] > list[i + 1]:
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
        current_index += 1
    return list

test_array = [1, 3, 2, 5, 4, 10, 11, 8, 7, 101, 6]
print(bubble(test_array))