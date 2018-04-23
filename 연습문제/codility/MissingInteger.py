def solution(array):

    if max(array) < 0:
        return 1

    for i in range(1, max(array) + 1):
        print(i)
        if i in array:
            continue
        else:
            return i

    return max(array) + 1


