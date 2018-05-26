from collections import deque


def solution(number, direction, k, j):
    people = generate_array(number)
    people_deque = deque(people)
    current_step = k
    direction_argument = 0

    if direction == 0:
        direction_argument = 1

    else:
        direction_argument = -1


    while(len(people_deque) > 1):
        people_deque.rotate(current_step * direction_argument)
        people_deque.popleft()
        people_deque.rotate(direction_argument * -1)
        current_step += j

    print("answer: ", people_deque.pop())


def generate_array(number):
    people = []

    for i in range(0, number):
        people.append(i + 1)
    return people

def parse(string):
    list_input = string.split(" ")
    return_array = []

    for input_number in list_input:
        return_array.append(int(input_number))

    solution(return_array[0], return_array[1], return_array[2], return_array[3])

parse("6 1 1 1")
parse("6 1 2 1")
parse("6 1 1 2")
parse("4 0 2 2")


