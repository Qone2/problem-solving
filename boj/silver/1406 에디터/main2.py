import sys

input = sys.stdin.readline


class Node:
    def __init__(self, val) -> None:
        self.left = None
        self.left = None
        self.right = None
        self.val = val


if __name__ == "__main__":
    buffer = input()[:-1]
    first = None
    last = None
    tmp = None
    for i in range(len(buffer)):
        if i == 0:
            first = Node(buffer[i])
            tmp = first
            continue
        current = Node(buffer[i])
        tmp.right = current
        current.left = tmp
        tmp = current
        if i == len(buffer) - 1:
            last = current
            continue

    cursor = Node(None)
    last.right = cursor
    cursor.left = last

    N = int(input())
    for _ in range(N):
        command = input()
        if command[0] == 'L':
            if cursor.left is None:
                continue
            cursor = cursor.left
        elif command[0] == 'D':
            if cursor.val is None:
                continue
            cursor = cursor.right
        elif command[0] == 'B':
            if cursor.left is None:
                continue
            will_deleted = cursor.left
            cursor.left = will_deleted.left
            if will_deleted.left is None:
                first = cursor
                continue
            will_deleted.left.right = cursor
        elif command[0] == 'P':
            will_added = Node(command[2])
            will_added.left = cursor.left
            will_added.right = cursor
            cursor.left = will_added
            if will_added.left is None:
                first = will_added
                continue
            will_added.left.right = will_added

    tmp = first
    while tmp.val is not None:
        print(tmp.val, end='')
        tmp = tmp.right
