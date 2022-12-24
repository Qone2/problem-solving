from collections import deque
from typing import *


def solution(n: int, computers: List[List[int]]):
    """
    전체적으로 모든 vertex에 대하여 bfs를 하고 그 횟수를 샌다
    """
    answer = 0
    # visited 선언
    visited = list(False for _ in range(n))
    # 모든 정점에 대하여 bfs실행(방문한건 제외)
    for v in range(n):
        if visited[v]:
            continue
        # 큐 선언
        queue: Deque[int] = deque()
        # 정점을 방문 처리 후 큐에 넣고
        visited[v] = True
        queue.append(v)
        # 큐가 빌때까지
        while queue:
            # 하나 팝해서 연결된 정점들 중 방문하지 않은 정점들을 방문 처리 후 삽입
            current_v = queue.popleft()
            for i in range(n):
                if i == current_v:
                    continue
                if visited[i] is False and computers[current_v][i] == 1:
                    visited[i] = True
                    queue.append(i)

        # 한번 다 하면 answer+1
        answer += 1

    return answer


if __name__ == "__main__":
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
