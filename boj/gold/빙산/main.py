from typing import *
from collections import deque
import sys

input = sys.stdin.readline


def solution(graph: List[List[int]]) -> int:
    # time 선언
    time = 0
    # while True
    while True:
        # 빙산 개수 새기
        count = count_bfs(graph)
        # count 해서 0 나오면 break
        if count == 0:
            break
        if count >= 2:
            return time
        # 빙산 녹이고 시간 1증가
        graph = meltdown(graph)
        time += 1
    return 0


def count_bfs(graph: List[List[int]]) -> int:
    count = 0
    # 방문여부 선언
    visited = list(list(False for _ in range(len(graph[0]))) for _ in range(len(graph)))
    # 모든 칸에 대하여 BFS
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if bfs(i, j, graph, visited):
                count += 1

    return count


def bfs(x: int, y: int, graph: List[List[int]], visited: List[List[int]]) -> bool:
    # 방문했거나, 빙하가 아니면 return False
    if visited[x][y] is True or graph[x][y] == 0:
        return False
    # 큐 선언
    queue: Deque[Tuple[int, int]] = deque()
    # dx dy 선언
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    # 시작지점 큐에 넣고
    queue.append((x, y))
    # 큐가 빌때까지
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 방문하지 않았고, 0이 아니면
            if not is_out(graph, nx, ny) and visited[nx][ny] is False and graph[nx][ny] != 0:
                # 방문 처리 후 큐에 삽입
                visited[nx][ny] = True
                queue.append((nx, ny))
    return True


def is_out(graph: List[List[int]], n: int, m: int) -> bool:
    return n < 0 or n >= len(graph) or m < 0 or m >= len(graph[0])


def meltdown(graph: List[List[int]]) -> List[List[int]]:
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    new_graph = list(graph[i][:] for i in range(len(graph)))
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 0:
                continue
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if not is_out(graph, ni, nj) and graph[ni][nj] == 0:
                    if new_graph[i][j] > 0:
                        new_graph[i][j] -= 1
    return new_graph


if __name__ == "__main__":
    N, M = map(int, input().strip().split())
    problem_map = list(list(map(int, input().split())) for _ in range(N))
    print(solution(problem_map))
