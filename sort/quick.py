def quick_sort(list):

    if(len(list) < 2):
        return list

    else:
        pivot = list[0]

        smaller = [i for i in list[1:] if i <= pivot]
        greater = [i for i in list[1:] if i > pivot]

    return quick_sort(smaller) + quick_sort([pivot]) + quick_sort(greater)


print(quick_sort([10, 13, 12, 11, 9]))