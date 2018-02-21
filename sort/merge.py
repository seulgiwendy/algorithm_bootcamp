def merge_sort(list):

    if len(list) < 2:
        return list

    middle_index = len(list) // 2
    print(middle_index)

    left = merge_sort(list[:middle_index])
    right = merge_sort(list[middle_index:])

    left_index = 0
    right_index = 0
    whole_list_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            list[whole_list_index] = left[left_index]
            left_index += 1

        else:
            list[whole_list_index] = right[right_index]
            right_index += 1

        whole_list_index += 1

    if left_index == len(left):
        while right_index < len(right):
            list[whole_list_index] = right[right_index]
            right_index += 1
            whole_list_index += 1

    elif right_index == len(right):
        while left_index < len(left):
            list[whole_list_index] = left[left_index]
            left_index += 1
            whole_list_index += 1

    return list

print(merge_sort([3, 4, 1, 2, 10, 8, 145, 14]))

