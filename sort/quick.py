def quick_sort(list):

    if(len(list) < 2):
        return list

    else:
        pivot = list[0]

        smaller = []
        greater = []

        for i in range(1, len(list)):
            if list[i] <= pivot:
                smaller.append(list[i])
            else:
                greater.append(list[i])

    return quick_sort(smaller) + quick_sort([pivot]) + quick_sort(greater)


print(quick_sort([10, 13, 12, 11, 9, 8, 1, 4, 3]))