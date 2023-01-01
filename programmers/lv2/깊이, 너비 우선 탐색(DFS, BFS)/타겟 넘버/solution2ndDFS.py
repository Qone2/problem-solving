from typing import *


def solution(numbers, target):
    answer = 0
    # numbers for문 dfs로 처리
    answer = dfs(0, 0, target, numbers)

    return answer


def dfs(idx, current, target, numbers):
    # 종료조건: 목표값에 도달하면 종료
    if idx >= len(numbers) and current == target:
        return 1
    # 종료조건: idx가 끝이면 종료
    if idx >= len(numbers):
        return 0
    return dfs(idx + 1, current + numbers[idx], target, numbers) + dfs(idx + 1, current - numbers[idx], target, numbers)


if __name__ == "__main__":
    print(solution([1, 1, 1, 1, 1], 3))
    print(solution([4, 1, 2, 1], 4))
