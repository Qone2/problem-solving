import sys

# input = sys.stdin.readline

if __name__ == "__main__":
    text = input()[:-1]
    N = int(input())
    cursor = len(text)
    for _ in range(N):
        command = input()
        if command[0] == 'L':
            cursor = cursor - 1 if cursor != 0 else 0
        elif command[0] == 'D':
            cursor = cursor + 1 if cursor != len(text) else len(text)
        elif command[0] == 'B':
            if cursor == 0:
                continue
            text = text[0:cursor - 1] + text[cursor:]
            cursor -= 1
        elif command[0] == 'P':
            text = text[0:cursor] + command[2] + text[cursor:]
            cursor += 1

    print(text)
