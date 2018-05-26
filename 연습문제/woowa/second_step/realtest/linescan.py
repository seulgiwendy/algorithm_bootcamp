from collections import namedtuple

Range = namedtuple('Range', 'xmin xmax')

def solution(array):
    points = []
    intersects = []
    filtered_intersects = []
    for point in array:
        if len(point) == 1:
            points.append(Range(point[0], point[0]))
            continue
        points.append(Range(point[0], point[1]))

    points.sort()

    for i in range(len(points)):
        calculated_intersect = []
        start_point = points[i]
        print("start point is: ", start_point)

        for j in range(len(points)):

            if j == i :
                continue
            compare_point = points[j]

            start_set = to_intlist(start_point)
            compare_set = to_intlist(compare_point)

            intersect_points = list(set(start_set).intersection(compare_set))
            calculated_intersect.append(intersect_points)

        intersects.append(calculated_intersect)

    print(intersects)
    for intersect in intersects:
        for point in intersect:
            if len(point) > 0:
                filtered_intersects.append(point)


    print(filtered_intersects)

    for i in range(len(filtered_intersects) - 1):
        print(i)
        compare_element = filtered_intersects[i]

        for j in range(i + 1, len(filtered_intersects)):
            if filtered_intersects[j] == compare_element:
                filtered_intersects[j] = 0

    print(filtered_intersects)

def parse(string):
    str_list = string.split("\n")
    coords = []


    for splitted in str_list:
        append_list = []
        points = splitted.split(" ")

        for point in points:
            append_list.append(int(point))

        coords.append(append_list)

    solution(coords)

def to_intlist(delivered_range):
    int_list = []
    for i in range(delivered_range.xmin, delivered_range.xmax + 1):
        int_list.append(i)

    return int_list


print(parse("3\n1 3\n2 4\n5 6"))
