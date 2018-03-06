def pow(num, power):

    if power < 2:
        return num

    return num * pow(num, power - 1)

print(pow(3, 4))