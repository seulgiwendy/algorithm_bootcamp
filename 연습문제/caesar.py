def caesar(s, n):
    string_array = split_string(s)
    encrypted_array = return_encrypted(string_array, n)

    result = str.join("", encrypted_array)
    return result
    # 주어진 문장을 암호화하여 반환하세요.


# 실행을 위한 테스트코드입니다.
# print('s는 "a B z", n은 4인 경우: ' + caesar("a B z", 4))

def split_string(string):
    return list(string)

def return_encrypted(array, n):
    encrypted_char = []
    for char in array:
        origin_value = ord(char)
        next_value = origin_value + (n % 26)

        if(origin_value == 32):
            encrypted_char.append(chr(32))
            continue

        if(origin_value > 64 and origin_value < 91):
            if next_value > 90:
                next_value = next_value - 26

        if(origin_value > 96 and origin_value < 123):
            if next_value > 122:
                next_value = next_value - 26

        print(next_value)
        encrypted_char.append(chr(next_value))

    return encrypted_char



print(caesar("KouIeeyXQeJDanekJ mbnPgov lsuNNZKwkZpLwxqARNYuCyx", 129))