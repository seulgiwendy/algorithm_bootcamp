def binary_search(list, search, start, end):

    mid = start + end // 2
    if mid == 0:
        if list[mid] == search:
            return mid
        else:
            return None

    if mid > len(list) - 1:
        return None

    guess = list[mid]

    print(guess)

    if guess == search:
        return mid

    if guess < search:
        print(list[start:])
        return binary_search(list, search, start + 1, end)

    else:
        print(list[:end])
        return binary_search(list, search, start , end - 1)



my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

print("your target is at the index:" , binary_search(my_list, 11, 0, len(my_list) - 1))
