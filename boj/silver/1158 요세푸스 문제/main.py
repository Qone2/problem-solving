if __name__ == "__main__":
    N, K = map(int, input().split())
    arr = list(i + 1 for i in range(N))
    tmp = 0
    print('<', end='')
    while arr:
        if len(arr) != N:
            print(', ', end='')
        tmp += K - 1
        tmp = tmp % len(arr)
        print(arr.pop(tmp), end='')
    print('>')
