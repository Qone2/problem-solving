from collections import deque


def solution():
    n, m = map(int, input().split())
    queue = deque()
    priorities = list(map(int, input().split()))
    for i, p in enumerate(priorities):
        queue.append((p, i))

    count = 1
    while queue:
        max_v = max(queue)[0]
        if queue[0][0] < max_v:
            tmp = queue.popleft()
            queue.append(tmp)
            continue
        tmp = queue.popleft()
        if tmp[1] == m:
            return count
        count += 1


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        print(solution())
