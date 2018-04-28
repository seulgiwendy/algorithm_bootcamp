def solution(n, words):
    duplicate_index = check_duplicate(words)
    invalid_index = check_valid(words)

    if duplicate_index != 0:
        return check_turn(words, n, duplicate_index)

    if invalid_index != 0:
        return check_turn(words, n, invalid_index)

    return [0, 0]

def check_duplicate(array):
    words = []

    for i in range(len(array)):
        if array[i] in words:
            return i
        words.append(array[i])

    return 0

def check_valid(array):
    for i in range(len(array) - 1):
        if to_ord(array[i], True) != to_ord(array[i + 1], False):
            return i + 1

    return 0



def check_turn(array, n, i):
    print(n, i)
    turn = (i % n) + 1
    attempt = (i // n) + 1

    return [turn, attempt]



def to_ord(letter, is_first):
    chr_list = list(letter)

    if is_first:
        return ord(chr_list[-1])

    return ord(chr_list[0])

print(solution(3, ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']))



