from typing import *


def solution(prices: List[int]):
    answer = list(0 for _ in range(len(prices)))
    # 스택 선언
    stack: List[Tuple[int, int]] = []
    # prices에 대하여 순회
    for i in range(len(prices)):
        # while 스택에 있는 가격과 현재 가격을 비교, 현재가 더 싸면
        while len(stack) > 0 and stack[-1][1] > prices[i]:
            # answer에서 그 스택에 있는 위치의 초를 변경
            past_location, _ = stack.pop()
            answer[past_location] = i - past_location
        # 스택에 위치와 가격을 기록
        stack.append((i, prices[i]))
    # 끝까지 다 돌았으면 스택을 다 돌면서 끝시점으로 기록
    for location, _ in stack:
        answer[location] = len(prices) - 1 - location

    return answer


if __name__ == "__main__":
    print(solution([1, 2, 3, 2, 3]))
