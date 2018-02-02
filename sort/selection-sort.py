def findSmallest(list):

    smallest = list[0]
    smallest_index = 0

    for i in range(1, len(list)):

        if list[i] < smallest:
            smallest = list[i]
            smallest_index = i;

    return smallest_index

def selection_sort(list):
    newArray = []
    for i in range(len(list)):
        print("current list elements are ; ", list)
        smallest = findSmallest(list)
        newArray.append(list.pop(smallest))
        print(newArray)

    return newArray

print(selection_sort([1, 5, 3, 8, 7,]))