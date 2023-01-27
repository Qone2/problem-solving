import sys

input = sys.stdin.readline


def stack_print(num_of_command: int):
    stack = []
    for _ in range(N):
        instruction = input().split()
        if instruction[0] == "push":
            stack.append(instruction[1])
        elif instruction[0] == "pop":
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop())
        elif instruction[0] == "size":
            print(len(stack))
        elif instruction[0] == "empty":
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif instruction[0] == "top":
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])


if __name__ == "__main__":
    N = int(input())
    stack_print(N)
