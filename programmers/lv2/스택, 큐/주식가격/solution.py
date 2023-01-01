def solution(prices):
    answer = []
    for i in range(len(prices)):
        temp = prices[i]
        count = -1
        for j in range(i, len(prices)):
            count += 1
            if temp > prices[j]:
                break

        answer.append(count)

    return answer


if __name__ == "__main__":
    print(solution([1, 2, 3, 2, 3]))
