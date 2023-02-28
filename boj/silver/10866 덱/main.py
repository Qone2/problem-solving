import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    dq = deque()
    for _ in range(N):
        command = input()
        if command[0] == 'p':
            if command[1] == 'u':
                if command[5] == 'b':
                    dq.append(int(command[10:]))
                elif command[5] == 'f':
                    dq.appendleft(int(command[10:]))
            elif command[1] == 'o':
                if command[4] == 'f':
                    print(dq.popleft() if dq else -1)
                elif command[4] == 'b':
                    print(dq.pop() if dq else -1)
        elif command[0] == 's':
            print(len(dq))
        elif command[0] == 'e':
            print(0 if dq else 1)
        elif command[0] == 'f':
            print(dq[0] if dq else -1)
        elif command[0] == 'b':
            print(dq[-1] if dq else -1)
