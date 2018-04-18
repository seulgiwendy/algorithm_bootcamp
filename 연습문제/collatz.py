def collatz(num):
    answer = 0
    return find_by_recurse(num, 0)

def find_by_recurse(n, attempt):
    current_attempt = attempt

    if attempt > 500:
        return -1

    if n == 1:
        return attempt

    elif n % 2 == 0:
        return find_by_recurse(n / 2, current_attempt + 1)

    else:
        return find_by_recurse((n * 3) + 1, current_attempt + 1)


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(collatz(6))