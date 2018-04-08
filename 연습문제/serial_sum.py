def expressions(num):
    answer = 1
    sum = 0
    left = 0

    while left != num // 2 + 1 :
        print('left: ' , left)

        if sum < num:
            for right in range(left + 1, num // 2 + 2):
                print('right: ', right)
                sum += right
                print('sum: ', sum)
                if sum == num:
                    answer += 1
                    left += 1
                    sum = 0
                    break
                elif sum > num:
                    left += 1
                    sum = 0
                    break

    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(expressions(15));
