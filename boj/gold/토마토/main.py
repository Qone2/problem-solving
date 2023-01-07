from typing import *
from collections import deque
import sys

input = sys.stdin.readline


def checkout(boxes: List[List[List[int]]]):
    """
    전부 순회해서 최대값 찾기 0 이 있으면 -1 출력
    """
    max_v = -100
    for z in range(len(boxes)):
        for x in range(len(boxes[0])):
            for y in range(len(boxes[0][0])):
                if boxes[z][x][y] == 0:
                    print(-1)
                    return
                if boxes[z][x][y] > max_v:
                    max_v = boxes[z][x][y]
    print(max_v - 1)


def bfs(boxes: List[List[List[int]]], starts: List[Tuple[int, int, int]]):
    # 방문여부 선언
    visited = list(
        list(list(False for _ in range(len(boxes[0][0]))) for _ in range(len(boxes[0]))) for _ in range(len(boxes)))
    # 큐 선언
    queue: Deque[Tuple[int, int, int]] = deque()
    # 시작지점들 삽입
    # 방문처리도
    for z, x, y in starts:
        queue.append((z, x, y))
        visited[z][x][y] = True
    dz = [0, 0, 0, 0, 1, -1]
    dx = [0, 1, 0, -1, 0, 0]
    dy = [1, 0, -1, 0, 0, 0]
    # 큐가 빌때까지
    while queue:
        z, x, y = queue.popleft()
        # 주변에 대하여 방문 안했으면 방문처리 후 토마토 처리해주고 삽입
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if is_valid(boxes, visited, nz, nx, ny):
                visited[nz][nx][ny] = True
                boxes[nz][nx][ny] = boxes[z][x][y] + 1
                queue.append((nz, nx, ny))


def is_valid(boxes: List[List[List[int]]], visited, h, n, m):
    return not is_out(boxes, h, n, m) and visited[h][n][m] is False and boxes[h][n][m] == 0


def is_out(boxes: List[List[List[int]]], h, n, m):
    return h < 0 or n < 0 or m < 0 or h >= len(boxes) or n >= len(boxes[0]) or m >= len(boxes[0][0])


if __name__ == "__main__":
    M, N, H = map(int, input().split())
    boxes = list(list(list(map(int, input().split())) for _ in range(N)) for _ in range(H))
    starts = list()
    for z in range(H):
        for x in range(N):
            for y in range(M):
                if boxes[z][x][y] == 1:
                    starts.append((z, x, y))
    bfs(boxes, starts)
    checkout(boxes)
