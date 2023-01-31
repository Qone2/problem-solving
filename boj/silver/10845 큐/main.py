import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    queue = deque()
    for _ in range(N):
        command = input()
        if command[:2] == "pu":
            queue.append(int(command[5:]))
        elif command[:2] == "po":
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        elif command[:1] == "f":
            if queue:
                print(queue[0])
            else:
                print(-1)
        elif command[:1] == "b":
            if queue:
                print(queue[-1])
            else:
                print(-1)
        elif command[:1] == "s":
            print(len(queue))
        elif command[:1] == "e":
            print(1 if not queue else 0)
