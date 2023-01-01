from collections import deque


def solution(n, computers):
    answer = 0
    visited = list(False for _ in range(n))
    for i in range(n):
        if visited[i] is False:
            bfs(computers, i, visited)
            answer += 1

    return answer


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i, node in enumerate(graph[v]):
            if i == v:
                continue
            if node == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True
