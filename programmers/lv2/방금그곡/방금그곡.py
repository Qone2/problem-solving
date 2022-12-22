# class Data:
#     def __init__(self, arr):
#         self.time1 = arr[0]
#         self.time2 = arr[1]
#         self.name = arr[3]
#         self.melo = arr[4]




def solution(m, musicinfos):
    
    for arr in musicinfos:
        
        mellody = ""
        result = ""
        mellodylist = []
        mlist = []
        
        time1, time2, name, mellody = arr.split(',')
        timelong = int(time2.replace(":",""))-int(time1.replace(":",""))+1

        mellody = mellody*(int((timelong/len(mellody)))+1)

        for i in range(len(mellody)):
            if i != len(mellody)-1: 
                if mellody[i+1] == "#":
                    mellodylist.append(mellody[i]+mellody[i+1])
                else:
                    mellodylist.append(mellody[i])
            elif i == len(mellody)-1:
                 mellodylist.append(mellody[i])

        for i in range(len(m)):
            if i != len(m)-1:
                if m[i+1] == "#":
                    mlist.append(m[i]+m[i+1])
                else:
                    mlist.append(m[i])
            elif i == len(m)-1:
                 mlist.append(m[i])
        mlist.append("0")
        mellodylist.append("#")

        # print(mlist)
        # print(mellodylist)
        
        mylong = len(m)

        if musicfind(mlist,mellodylist) and timelong > mylong:
            #찾았다!
            
            return name
    
    return "`(None)`"


def musicfind(mlist, mellodylist):
    i = 0
    j = 0
    while j < len(mellodylist)-1:
        while mlist[i] != mellodylist[j]:
            j = j+1
            # print("j값 올리는중")
            if j >= len(mellodylist)-1:
                # print("아이씨 뭐야 j 왤케 높아")
                break
            # print("첫번째 거 찾았어")
        
        while mlist[i] == mellodylist[j]:
            i = i + 1
            j = j + 1
        
        if i == len(mlist)-1:
            # print("찾았다!")
            return True
        else:
            i = 0
            continue
    # print("헉 다 끝나버렸는데 없엉")

    return False
    
