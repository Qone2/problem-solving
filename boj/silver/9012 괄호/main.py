import sys

input = sys.stdin.readline


def vps(s: str):
    stack = 0
    for c in s:
        if c == '(':
            stack += 1
        elif c == ')':
            if stack < 1:
                print("NO")
                return
            stack -= 1

    print("YES" if stack == 0 else "NO")


if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        vps(input())
