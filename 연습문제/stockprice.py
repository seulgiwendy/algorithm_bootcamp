def solution(prices):
    answer = []

    for i in range(len(prices)):
        remaining_prices = prices[i + 1:]
        time_count = 0

        if i == len(prices) - 1:
            answer.append(time_count)
            return answer

        for j in range(len(remaining_prices)):
            time_count += 1

            if prices[i] > remaining_prices[j]:
                answer.append(time_count)
                break

            if j == len(remaining_prices) - 1:
                answer.append(time_count)
                break

    return answer
