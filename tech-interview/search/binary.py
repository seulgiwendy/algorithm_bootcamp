def search(array, target, start, end):
    print(start, end)

    if start > end:
        return None

    mid = (start + end) // 2

    if mid == 0:
        if array[mid] == target:
            return 0

        else:
            return None

    if mid >= len(array):
        return None

    guess = array[mid]

    if guess == target:
        return mid

    if target > guess:
        return search(array, target, mid + 1, end)

    if target < guess:
        return search(array, target, start, mid - 1)

    return 0

test = [1, 2, 3, 4, 5]

print(test[3:])
print(test[:3])

print(search(test, 6, 0, len(test) - 1))