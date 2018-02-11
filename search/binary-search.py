def binary_search(list, search, start, end):
    mid = (start + end) // 2
    print(mid)
    if mid == 0:
        if list[mid] == search:
            return mid
        else:
            return None

    if mid >= len(list):
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

print("your target is at the index:" , binary_search(my_list, 999, 0, len(my_list)))
