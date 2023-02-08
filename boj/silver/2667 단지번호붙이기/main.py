from collections import deque
from typing import *
import sys


# input = sys.stdin.readline


def solution(graph: List[List[int]]):
    answer_list = []
    visited = list(list(False for _ in range(len(graph[0]))) for _ in range(len(graph)))
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if not visited[i][j] and graph[i][j] == 1:
                answer_list.append(bfs(i, j, graph, visited))
    answer_list.sort()
    print(len(answer_list))
    for a in answer_list:
        print(a)


def bfs(x, y, graph: List[List[int]], visited: List[List[bool]]):
    queue: Deque[Tuple[int, int]] = deque()
    visited[x][y] = True
    queue.append((x, y))
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    count = 1

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))
                count += 1
    return count


if __name__ == "__main__":
    N = int(input())
    graph = list(list(map(int, list(c for c in input()))) for _ in range(N))
    solution(graph)
