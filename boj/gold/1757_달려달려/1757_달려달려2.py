import sys
sys.stdin = open("input.txt", 'r')
sys.stdout = open("output.txt", 'w')

N, M = map(int, input().split())
D_arr = [0]
for _ in range(N):
    D_arr.append(int(input()))

dp = list(list(list(0 for _ in range(2)) for _ in range(M + 5)) for _ in range(2))

for i in range(1, N + 1):
    for j in range(M + 1):
        if j == 0:
            dp[i % 2][j][0] = max(dp[i % 2 - 1][j + 1][0], dp[i % 2 - 1][j][0], dp[i % 2 - 1][j + 1][1])
            continue
        if j == 1:
            dp[i % 2][j][1] = dp[i % 2 - 1][j - 1][0] + D_arr[i]
            dp[i % 2][j][0] = max(dp[i % 2 - 1][j + 1][1], dp[i % 2 - 1][j + 1][0])
            continue
        dp[i % 2][j][1] = dp[i % 2 - 1][j - 1][1] + D_arr[i]
        dp[i % 2][j][0] = max(dp[i % 2 - 1][j + 1][1], dp[i % 2 - 1][j + 1][0])

print(dp[N % 2][0][0])
