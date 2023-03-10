import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    stack = []
    for _ in range(N):
        num = int(input())
        if num == 0:
            stack.pop()
            continue
        stack.append(num)
    print(sum(stack))
