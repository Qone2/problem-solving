import heapq
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    # 전체를 절반으로 나눴을때 최대힙에는 낮은 절반
    # 최소힙에는 큰 절반이 들어가도록 조정
    # 그 후 최대힙의 첫번쨰 값이 중간갑
    N = int(input())
    max_heap = []
    min_heap = []
    for _ in range(N):
        current = int(input())
        if len(max_heap) <= len(min_heap):
            heapq.heappush(max_heap, -current)
        else:
            heapq.heappush(min_heap, current)
        if max_heap and min_heap and -max_heap[0] > min_heap[0]:
            low = heapq.heappop(min_heap)
            high = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, high)
            heapq.heappush(max_heap, -low)
        print(-max_heap[0])
