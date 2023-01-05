from typing import *
from collections import deque
import sys

sys.stdin = open("input.txt", 'r')
sys.stdout = open("output.txt", 'w')
input = sys.stdin.readline


def bfs(graph: List[List[int]], n, m) -> int:
    # 방문여부 선언
    visited: List[List[bool]] = list(list(False for _ in range(m)) for _ in range(n))
    # 큐 선언
    queue: Deque[Tuple[int, int, int]] = deque()
    # 첫 지점 방문처리 후 큐에 삽입
    visited[0][0] = True
    queue.append((0, 0, 1))
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    # 큐가 빌때까지
    while queue:
        # 팝 하고 조건에 맞으면 count 리턴
        x, y, count = queue.popleft()
        if x == n - 1 and y == m - 1:
            return count
        # 인접노드에 대하여 유효하고 방문안한곳에 대하여 방문처리 후 큐에 삽입
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_valid(graph, nx, ny) and visited[nx][ny] is False:
                visited[nx][ny] = True
                queue.append((nx, ny, count + 1))
    return -1


def is_valid(graph: List[List[int]], n, m) -> bool:
    return not is_out(graph, n, m) and graph[n][m] == 1


def is_out(graph: List[List[int]], n, m) -> bool:
    return n < 0 or n >= len(graph) or m < 0 or m >= len(graph[0])


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph: List[List[int]] = list(list(0 for _ in range(M)) for _ in range(N))
    for i in range(N):
        string = input()
        for j in range(M):
            graph[i][j] = int(string[j])
    print(bfs(graph, N, M))
