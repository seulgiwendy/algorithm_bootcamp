def solution(S):
    character_array = list(S)

    if len(character_array) % 2 != 0:
        return 0

    character_ascii_array = [ord(c) for c in character_array]

    character_stack = []

    for ascii in character_ascii_array:
        if ascii == 40 or ascii == 91 or ascii == 123:
            character_stack.append(ascii)
            continue

        if ascii == 41:

            if len(character_stack) == 0:
                return 0

            if character_stack.pop() == 40:
                continue
            return 0

        if ascii == 93:

            if len(character_stack) == 0:
                return 0

            if character_stack.pop() == 91:
                continue
            return 0

        if ascii == 125:

            if len(character_stack) == 0:
                return 0

            if character_stack.pop() == 123:
                continue
            return 0

    if len(character_stack) > 0:
        return 0

    return 1


print(solution("{[()()]}"))
print(solution)
