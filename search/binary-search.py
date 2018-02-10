def binary_search(list, search, start, end):
    mid = (start + end) // 2
    if mid == 0:
        if list[mid] == search:
            return mid
        else:
            return None

    if mid > end:
        return None

    guess = list[mid]

    if guess == search:
        return mid

    if guess < search:
        return binary_search(list, search, mid + 1, end)

    else:
        return binary_search(list, search, start, mid - 1)

my_list = []

for i in range(1024):
    my_list.append(i + 1)

print("your target is at the index:" , binary_search(my_list, 131, 0, len(my_list)))
