import sys

# input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    words = set(input() for _ in range(N))
    words = list(words)
    words.sort()
    words.sort(key=len)

    for word in words:
        print(word)
