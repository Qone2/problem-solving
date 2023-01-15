import sys
sys.stdin = open("input.txt", 'r')
sys.stdout = open("output.txt", 'w')

N = int(input())

dp = list(-1 for _ in range(N + 1))
dp[1] = 0
dp[2] = 1
dp[3] = 1
dp[4] = 2


def foo(n):
    if dp[n] != -1:
        return dp[n]
    if n % 3 == 0 and n % 2 == 0:
        dp[n] = min(foo(n // 3), foo(n // 2), foo(n - 1)) + 1
        return dp[n]
    if n % 3 == 0:
        dp[n] = min(foo(n // 3), foo(n - 1)) + 1
        return dp[n]
    if n % 2 == 0:
        dp[n] = min(foo(n // 2), foo(n - 1)) + 1
        return dp[n]
    dp[n] = foo(n-1) + 1
    return dp[n]


for i in range(5, N + 1):
    foo(i)
print(foo(N))
