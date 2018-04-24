def solution(n, array):
    counters = counter_init(n)

    for number in array:
        if number > 0 and number < n + 1:
            counters[number - 1] += 1

        else:
            counters = max_counters(counters)

    return counters


def counter_init(length):
    new_counter = []

    for i in range(length):
        new_counter.append(0)

    return new_counter

def max_counters(array):
    max_value = max(array)

    for i in range(len(array)):
        array[i] = max_value
    return array


