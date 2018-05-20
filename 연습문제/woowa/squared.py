import itertools
import math


def solution(a, b, c, d):
    combinations = []

    for subset in itertools.combinations([a, b, c, d], 2):
        combinations.append(subset)

    return calculate_distance(combinations)

def calculate_distance(array):

    current_pointer = len(array) - 1
    results = []

    while(current_pointer > -1):
        origin_point = array[current_pointer]

        for plots in array:
            if plots == origin_point:
                continue

            x_distance = math.pow(origin_point[0] - plots[0], 2)
            y_distance = math.pow(origin_point[1] - plots[1], 2)


            results.append(int((x_distance + y_distance)))


        current_pointer -= 1

    return max(results)

print(solution(2, 4, 2, 4))





