from collections import deque


if __name__ == "__main__":
    N = int(input())
    targets = deque(int(input()) for _ in range(N))
    stack = deque()

    target = targets.popleft()
    commands = list()
    i = 1
    while i < N + 1 or len(commands) < N * 2:
        if i <= target:
            stack.append(i)
            i += 1
            commands.append("+")
        elif stack[-1] == target:
            stack.pop()
            if targets:
                target = targets.popleft()
            commands.append('-')
        else:
            print("NO")
            exit()
    for c in commands:
        print(c)
