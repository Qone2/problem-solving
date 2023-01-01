from collections import deque
from typing import *


def solution(numbers, target):
    answer = 0
    # 큐 선언
    queue: Deque[Tuple[int, int]] = deque()

    # 초기값 삽입
    queue.append((0, 0))

    # 큐가 빌때까지
    while queue:
        idx, current = queue.popleft()
        # 종료조건1: 끝까지 다 더하고, 목표도달
        if idx >= len(numbers) and current == target:
            answer += 1
            continue
        # 종료조건2: 끝까지 갔을때
        if idx >= len(numbers):
            continue
        # 두가지 상황에 따라 더하기
        queue.append((idx + 1, current + numbers[idx]))
        queue.append((idx + 1, current - numbers[idx]))

    return answer


if __name__ == "__main__":
    print(solution([1, 1, 1, 1, 1], 3))
    print(solution([4, 1, 2, 1], 4))
