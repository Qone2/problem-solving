from typing import *
from collections import defaultdict, deque
import sys

input = sys.stdin.readline


def dfs(adj_lists: Dict[int, List[int]], n, start):
    visited = list(False for _ in range(n + 1))
    dfs_recursion(adj_lists, visited, start)
    print()


def dfs_recursion(adj_lists: Dict[int, List[int]], visited: List[bool], current):
    # 현재노드 방문처리
    visited[current] = True
    print(current, end=" ")
    # 인접 노드 중 방문하지 않은 노드 dfs 재귀
    for node in adj_lists[current]:
        if visited[node] is False:
            dfs_recursion(adj_lists, visited, node)


def bfs(adj_lists: Dict[int, List[int]], n, start):
    # 방문여부 선언
    visited = list(False for _ in range(n + 1))
    # 큐 선언
    queue = deque()
    # 첫지점 방문처리 후 큐에 삽입
    visited[start] = True
    queue.append(start)
    print(start, end=" ")
    # 큐가 빌때까지
    while queue:
        current = queue.popleft()
        for node in adj_lists[current]:
            if visited[node] is False:
                visited[node] = True
                queue.append(node)
                print(node, end=" ")
    print()


if __name__ == "__main__":
    N, M, S = map(int, input().split())
    adj_lists: Dict[int, List[int]] = defaultdict(list)
    for _ in range(M):
        a, b = map(int, input().split())
        adj_lists[a].append(b)
        adj_lists[b].append(a)
    for key in adj_lists:
        adj_lists[key].sort()
    dfs(adj_lists, N, S)
    bfs(adj_lists, N, S)
