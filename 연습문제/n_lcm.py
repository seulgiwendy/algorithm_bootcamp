def nlcm(num):
    return lcm_recurse(num)

def lcm_recurse(array):
    if len(array) == 1:
        return array[0]

    if len(array) == 2:
        return find_lcm(array[0], array[1])

    return find_lcm(array[-1], lcm_recurse(array[:-1]))

def find_lcm(num1, num2):
    gcd = find_gcd(num1, num2)

    return int(gcd * (num1 / gcd) * (num2 / gcd))

def find_gcd(num1, num2):
    current_divider = 0

    if num1 > num2:
        current_divider = num2
    else:
        current_divider = num1

    while(True):
        if num1 % current_divider == 0 and num2 % current_divider == 0:
            break;
        current_divider -= 1

    return int(current_divider)

print(nlcm([2, 6, 8, 14]))

