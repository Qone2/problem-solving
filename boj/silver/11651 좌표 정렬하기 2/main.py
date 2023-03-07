import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    coords = []
    for _ in range(N):
        coords.append(tuple(map(int, input().split())))
    coords.sort()
    coords.sort(key=lambda coord: coord[1])

    for coord in coords:
        print(coord[0], end=' ')
        print(coord[1])
