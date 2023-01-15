import sys
sys.stdin = open("input.txt", 'r')
sys.stdout = open("output.txt", 'w')


N = int(input())
conferences = list(list(map(int, input().strip().split())) for _ in range(N))
conferences = sorted(sorted(conferences), key=lambda c: c[1])

a = 0
b = 0
for con in conferences:
    if con[0] < b:
        continue
    b = con[1]
    a += 1
print(a)
