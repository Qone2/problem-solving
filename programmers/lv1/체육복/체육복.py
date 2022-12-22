lost = []
reserve = []

def solution(n, lost, reserve):
    cldic = {}
    for i in range(1,n+1):
        cldic[i] = 1
    
    for a in lost:
        cldic[a] -= 1

    for a in reserve:
        cldic[a] += 1
    

    for i in range(1,n):
        if cldic[i] == 0 and cldic[i+1] == 2:
            cldic[i] += 1
            cldic[i+1] -= 1

    for i in range(1,n):
        if cldic[i] == 2 and cldic[i+1] == 0:
            cldic[i] -= 1
            cldic[i+1] += 1

    if cldic[n] == 0 and cldic[n-1] == 2:
        cldic[n] += 1
        cldic[n-1] -= 1

    count = 0
    for i in range(1,n+1):
        if cldic[i] >= 1:
            count += 1
    
    return count
