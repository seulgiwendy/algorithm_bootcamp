import random


def quick_sort(list):

    random_index = 0

    if(len(list) < 2):
        return list

    else:
        random_index = random.randrange(0, len(list))

        pivot = list[random_index]

        smaller = []
        greater = []

        for i in range(0, len(list)):
            if i == random_index:
                continue
            if list[i] <= pivot:
                smaller.append(list[i])
            else:
                greater.append(list[i])

    return quick_sort(smaller) + quick_sort([pivot]) + quick_sort(greater)


print(quick_sort([10, 13, 12, 11, 9, 8, 1, 4, 3]))