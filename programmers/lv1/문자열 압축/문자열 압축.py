import math

def solution(s):
    sl = []
    datalist = []
    for idx in range(len(s)):
        for i in range(math.ceil(len(s)/(idx+1))):
            sl.append(s[i*(idx+1) : (i+1)*(idx+1)])

        datalist.append(sl)
        sl = []


    result = []

    for data in datalist:
        count = 0
        tmp = ""
        tmpc = ""
        for idx,d in enumerate(data):
            
            if idx == 0:
                if idx != len(data)-1:
                    count += 1
                    tmpc = d
                else:
                    tmp = d
            elif d == tmpc and idx != len(data)-1:
                count += 1
            elif d != tmpc and idx != len(data)-1:
                if count == 1:
                    tmp = tmp + tmpc
                    count = 1
                    tmpc = d
                else:
                    tmp = tmp + str(count) + tmpc
                    count = 1
                    tmpc = d
            elif idx == len(data)-1:
                if d != tmpc:
                    if count == 1:
                        tmp = tmp + tmpc
                        tmp = tmp + d
                    else:
                        tmp = tmp + str(count) + tmpc
                        tmp = tmp + d

                elif d == tmpc:
                    count += 1
                    tmp = tmp + str(count) + tmpc

        #print(tmp)
        result.append(len(tmp))
    print(result)

    return min(result)

            


