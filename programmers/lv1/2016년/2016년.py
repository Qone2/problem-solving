mounthday = [4,0,1,4,6,2,4,0,3,5,1,3]
day = 0


def solution(a, b):
    day = (mounthday[(a-1)]+(b-1))%7
    if day == 0:
        return "MON"
    elif day == 1:
        return "TUE"
    elif day == 2:
        return "WED"
    elif day == 3:
        return "THU"
    elif day == 4:
        return "FRI"
    elif day == 5:
        return "SAT"
    elif day == 6:
        return "SUN"


for i in range(12):
    print("%s 월" % (i+1))
    for j in range(31):
        print(solution(i+1,j+1),end=" ")
    print("")
    print("")
    print("")
