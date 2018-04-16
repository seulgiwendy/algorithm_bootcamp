import math

def numberOfPrime(n):
    # 1부터 n사이의 소수는 몇 개인가요?
    num_array = []

    divider = math.sqrt(n)

    if int(divider) < math.sqrt(n):
        divider += 1

    for i in range(1, n + 1):
        num_array.append(i)

    return count_sosu(eratostenes(num_array, int(divider)))

def eratostenes(array, multiplier):

    while multiplier > 1:
        print(multiplier)
        for i in range(len(array)):
            if array[i] == 1:
                array[i] = 0

            if array[i] % multiplier == 0 and array[i] != multiplier:
                array[i] = 0

        multiplier -= 1

    return array


def count_sosu(array):
    answer = 0

    for number in array:
        if number != 0:
            answer += 1

    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(numberOfPrime(161))