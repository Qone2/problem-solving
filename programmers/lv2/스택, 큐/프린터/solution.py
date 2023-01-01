from collections import deque
from typing import List, Tuple, Dict, Set, Deque


def solution(priorities: List[int], location):
    answer = 1
    waiting: Deque = deque()
    for i, p in enumerate(priorities):
        waiting.append((p, i))
    max_w = max(waiting)

    while len(waiting) > 0:
        max_w = max(waiting)
        current = waiting.popleft()
        if current[0] < max_w[0]:
            waiting.append(current)
            continue

        if current[1] == location:
            return answer
        answer += 1

    return answer


if __name__ == "__main__":
    print(solution([2, 1, 3, 2], 2))
    print(solution([1, 1, 9, 1, 1, 1], 0))
