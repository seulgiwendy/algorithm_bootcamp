def Harshad(n):
    divider = find_divider(n, 0)

    return n % divider == 0

def find_divider(n, last_digit):
    current_digit = last_digit

    if n < 10:
        current_digit += n
        return current_digit

    current_digit += n % 10

    return find_divider(n // 10, current_digit)

print(Harshad(18))

