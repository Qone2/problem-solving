import sys
sys.stdin = open("input.txt", 'r')
sys.stdout = open("output.txt", 'w')

N, M = map(int, input().strip().split())
che = list(list(input().strip()) for _ in range(N))
# for qwe in che:
#     print('[', end='')
#     for asd in qwe:
#         print("{0:>3}, ".format(asd), end='')
#     print(']')

minimum = 1234567890
for i in range(N-7):
    for j in range(M-7):
        tmpB = 0
        tmpW = 0
        tmp = 1234567890
        for x in range(8):
            for y in range(8):
                if che[i+x][j+y] == 'B' and (x+y) % 2 == 0:
                    pass
                elif che[i+x][j+y] == 'W' and (x+y) % 2 == 1:
                    pass
                else:
                    tmpB += 1
        for x in range(8):
            for y in range(8):
                if che[i+x][j+y] == 'W' and (x+y) % 2 == 0:
                    pass
                elif che[i+x][j+y] == 'B' and (x+y) % 2 == 1:
                    pass
                else:
                    tmpW += 1
        tmp = min(tmpB, tmpW)
        minimum = min(minimum, tmp)
print(minimum)
