import sys
sys.stdin = open("input.txt", 'r')
sys.stdout = open("output.txt", 'w')

N = int(input())

dp = list(-1 for _ in range(N + 1))
dp[1] = 0
dp[2] = 1
dp[3] = 1
dp[4] = 2


for i in range(5, N + 1):
    if dp[i] != -1:
        continue
    elif i % 3 == 0 and i % 2 == 0:
        dp[i] = min(dp[i // 3], dp[i // 2], dp[i - 1]) + 1
    elif i % 3 == 0:
        dp[i] = min(dp[i // 3], dp[i - 1]) + 1
    elif i % 2 == 0:
        dp[i] = min(dp[i // 2], dp[i - 1]) + 1
    else:
        dp[i] = dp[i - 1] + 1

print(dp[N])
