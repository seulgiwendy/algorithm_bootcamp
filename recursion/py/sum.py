def recursive_sum(list):
    if len(list) == 1:
        return list[0]

    return list[-1] + sum(list[:-1])

test_array = []

for i in range(1, 101):
    test_array.append(i)

print(recursive_sum(test_array))