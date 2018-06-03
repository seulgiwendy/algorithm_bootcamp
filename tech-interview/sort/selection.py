def selection(array):

    new_array = []

    while len(array) > 0:
        lowest_index = find_smallest(array)

        new_array.append(array.pop(lowest_index))

    return new_array

def find_smallest(list):
    smallest = list[0]
    smallest_index = 0

    for i in range(1, len(list)):
        if list[i] < smallest:
            smallest_index = i
            smallest = list[i]

    return smallest_index

print(selection([1, 3, 2, 4, 5, 8, 10, 9, 6, 7]))

