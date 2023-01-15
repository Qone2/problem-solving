import sys
sys.stdin = open("input.txt", 'r')
sys.stdout = open("output.txt", 'w')

N = int(input())
arr_N = list(map(int, input().split()))
M = int(input())
arr_M = list(map(int, input().split()))
arr_N.sort()


def bi_search(arr: list, wanted, low: int, high: int):
    mid = int((low + high) / 2)
    if high < low:
        return 0
    if arr[mid] == wanted:
        return 1
    elif arr[mid] < wanted:
        return bi_search(arr, wanted, mid + 1, high)
    elif arr[mid] > wanted:
        return bi_search(arr, wanted, low, mid - 1)


for a in arr_M:
    print(bi_search(arr_N, a, 0, N - 1))
