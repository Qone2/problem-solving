from collections import deque
import sys

input = sys.stdin.readline


def bfs(adj_list):
    visited = list(False for _ in range(len(adj_list)))
    queue = deque()
    visited[1] = True
    queue.append(1)
    count = 0
    while queue:
        current = queue.popleft()
        for node in adj_list[current]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)
                count += 1
    return count


if __name__ == "__main__":
    N = int(input())
    net_list = list(list() for _ in range(N + 1))
    n = int(input())
    for _ in range(n):
        src, dest = map(int, input().split())
        net_list[src].append(dest)
        net_list[dest].append(src)
    print(bfs(net_list))
