import sys
import heapq

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    result = 0
    decks = []
    for _ in range(N):
        heapq.heappush(decks, int(input()))
    while len(decks) > 1:
        d1 = heapq.heappop(decks)
        d2 = heapq.heappop(decks)
        current = d1 + d2
        result += current
        heapq.heappush(decks, current)
    print(result)
