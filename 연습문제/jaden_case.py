def Jaden_Case(s):
    # 함수를 완성하세요
    str_list = s.split(' ')

    character_list = []
    answer_list = []

    for string in str_list:
        character_list.append(list(string))

    for character in character_list:
        to_uppercase(character)

    for character in character_list:
        answer_list.append(''.join(character))


    return ' '.join(answer_list)

def to_uppercase(array):
    for i in range(len(array)):
        char_code = ord(array[i])

        if i == 0:
            if char_code < 123 and char_code > 96:
                array[i] = chr(char_code - 32)
            else:
                continue

        else:
            if char_code > 64 and char_code < 91:
                array[i] = chr(char_code + 32)

            else:
                continue


    return array



# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Jaden_Case("3people unFollowed me for the last week"))


