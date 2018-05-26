from collections import namedtuple
Rectangle = namedtuple('Rectangle', 'xmin ymin xmax ymax')

def area(a, b):
    dx = min(a.xmax, b.xmax) - max(a.xmin, b.xmin)
    dy = min(a.ymax, b.ymax) - max(a.ymin, b.ymin)
    if (dx>=0) and (dy>=0):
        return dx*dy

def position(a, b):
    xmaxpos = min(a.xmax, b.xmax)
    ymaxpos = min(a.ymax, b.ymax)

    xminpos = max(a.xmin, b.xmin)
    yminpos = max(a.ymin, b.ymin)

    return [xminpos, yminpos, xmaxpos, ymaxpos]

print(position(Rectangle(0, 50, 70, 90), Rectangle(40, 70, 90, 110)))

def solution(string):
    points_array = parse(string)

    first_rectangle = points_array[0:4]
    second_rectangle = points_array[4:8]
    last_rectangle = points_array[8:]

    origin_space = calculate_space(first_rectangle)
    first_intersect = area(Rectangle(first_rectangle[0], first_rectangle[1], first_rectangle[2], first_rectangle[3]), Rectangle(second_rectangle[0], second_rectangle[1], second_rectangle[2], second_rectangle[3]))
    second_intersect = area(Rectangle(first_rectangle[0], first_rectangle[1], first_rectangle[2], first_rectangle[3]), Rectangle(last_rectangle[0], last_rectangle[1], last_rectangle[2], last_rectangle[3]))
    last_intersect = area(Rectangle(second_rectangle[0], second_rectangle[1], second_rectangle[2], second_rectangle[3]), Rectangle(last_rectangle[0], last_rectangle[1], last_rectangle[2], last_rectangle[3]))
    last_post = position(Rectangle(second_rectangle[0], second_rectangle[1], second_rectangle[2], second_rectangle[3]), Rectangle(last_rectangle[0], last_rectangle[1], last_rectangle[2], last_rectangle[3]))

    final_intersect = area(Rectangle(last_post[0], last_post[1], last_post[2], last_post[3]), Rectangle(first_rectangle[0], first_rectangle[1], first_rectangle[2], first_rectangle[3]))

    print(last_post)


    if first_intersect == 0 or second_intersect == 0:
        return origin_space - first_intersect - second_intersect

    return origin_space - first_intersect - second_intersect + final_intersect


def parse(string):
    str_points = str.split(string, " ")

    points = []

    for point in str_points:
        points.append(int(point))

    return points


def calculate_space(array):

    first_x = array[0]
    second_x = array[2]
    third_x = second_x


    first_y = array[1]
    second_y=array[3]
    third_y = first_y

    return (third_x - first_x) * (second_y - third_y)

print(solution("700 400 1600 1100 0 400 1100 900 900 0 1800 650"))
print(solution("0 20 40 70 25 10 65 50 25 20 85 50"))
