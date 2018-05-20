def solution(s):
    stack = []
    commands = parse(s)

    for command in commands:

        if command == "DUP":
            stack.append(stack[-1])
            continue

        if command == "POP":
            stack.pop()
            continue

        if command == "+":
            first_number = stack.pop()
            second_number = stack.pop()

            stack.append(first_number + second_number)
            continue

        if command == "-":
            if(len(stack) < 2):
                return -1

            first_number = stack.pop()
            second_number = stack.pop()

            result = first_number - second_number

            if result < 0:
                return -1

            stack.append(result)
            continue

        else:
            stack.append(int(command))

    if len(stack) == 0:
        return -1

    return stack[-1]



def parse(string):
    return string.split(" ")


print(solution("13 DUP 4 POP 5 DUP + DUP + -"))
print(solution("5 6 + -"))
print(solution("3 DUP 5 - -"))