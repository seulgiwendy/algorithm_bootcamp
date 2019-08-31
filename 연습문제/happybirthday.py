import collections


def solution(phrases, second):
    max_disp_count = 14
    default_output = '_'

    disp_count = calculate_displayable_letters(second, phrases)
    blank_count = max_disp_count - disp_count

    answer_array = collections.deque([])

    for i in range(0, blank_count):
        answer_array.appendleft(default_output)

    answer_array.append(generate_display(phrases, disp_count))

    answer = ''.join(answer_array)
    return answer


def calculate_displayable_letters(second, phrase):
    if second == 14:
        return second

    if len(phrase) > 14 & second >= 14:
        if second - len(phrase) < 14:
            pass
        return 14

    return second % 14


def generate_display(phrases, displayable_letters):
    if displayable_letters == 0:
        return ''

    if len(phrases) == displayable_letters:
        return phrases

    if len(phrases) > displayable_letters:
        listed_phrase = list(phrases)
        return ''.join(listed_phrase[:displayable_letters])

    if len(phrases) < displayable_letters:
        listed_phrase = list(phrases)

        for i in range(len(listed_phrase), displayable_letters):
            listed_phrase.append('_')

            ''.join(listed_phrase)

        print listed_phrase
        return ''.join(listed_phrase)

def generate_long_display(phrases, displayable_letters):
    pass


print(solution('happy', 14))



