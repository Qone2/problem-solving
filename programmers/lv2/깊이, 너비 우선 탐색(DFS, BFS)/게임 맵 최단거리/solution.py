from collections import deque
from typing import List, Set, Tuple, Dict, Deque


def solution(maps: List[List[int]]):
    visited = list(list(False for _ in range(len(maps[0]))) for _ in range(len(maps)))
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 큐 선언
    queue: Deque[Tuple[int, int, int]] = deque()
    # 큐에 첫번째 노드 방문처리 후 큐에 삽입
    visited[0][0] = True
    queue.append((0, 0, 1))
    # 큐가 빌때까지
    while len(queue) > 0:
        x, y, time = queue.popleft()
        # 종료조건 끝지점이면 리턴
        if x == len(maps) - 1 and y == len(maps[0]) - 1:
            return time
        for i in range(4):
            # 유효하면 진행
            if is_valid(x + dx[i], y + dy[i], maps, visited):
                # 지점을 방문처리 후 큐에 삽입
                visited[x + dx[i]][y + dy[i]] = True
                queue.append((x + dx[i], y + dy[i], time + 1))

    return -1


def is_out(x: int, y: int, maps: List[List[int]]):
    return x < 0 or x >= len(maps) or y < 0 or y >= len(maps[0])


def is_valid(x, y, maps, visited):
    return not is_out(x, y, maps) and maps[x][y] != 0 and visited[x][y] is False


if __name__ == "__main__":
    print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
    print(solution([[1, 0, 1, 1, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 1, 1, 0], [1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 1, 1]]))
