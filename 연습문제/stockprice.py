def solution(prices):
    answer = []

    for i in range(len(prices)):

        for j in range(i + 1, len(prices)):

            print("i price: " + str(prices[i]))
            print("j price: " + str(prices[j]))

            if prices[i] > prices[j]:
                answer.append(j - i)

            if j == len(prices) - 1:
                answer.append(j - i)

    return answer


print(solution([1, 2, 3, 2, 3]))
