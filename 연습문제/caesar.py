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

    for str in array:
        str_code = ord(str)
        target_code = str_code + (n - 1)

        if(str_code == 32):
            encrypted_char.append(' ')

        if(str_code < 91 and target_code > 90):
            temporary_code = str_code + target_code % 26

            if(temporary_code > 90):
                target_code = temporary_code - 26
            else:
                target_code = temporary_code

        elif(str_code < 123 and target_code > 122):
            temporary_code = str_code + target_code % 26
            if(temporary_code > 122):
                target_code = temporary_code - 26
            else:
                target_code = temporary_code

        encrypted_char.append(chr(target_code))


    return encrypted_char


print(caesar("KouIeeyXQeJDanekJ mbnPgov lsuNNZKwkZpLwxqARNYuCyx", 29))