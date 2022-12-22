answers = []
score = [0,0,0]
yanswer = [2,1,2,3,2,4,2,5]
zanswer = [3,3,1,1,2,2,4,4,5,5]

def solution(answers):

    i = 1
    j = 0
    k = 0
    for a in answers:
        
        if i == a:
            score[0] += 1 
        i += 1
        if i == 6:
            i = 1
        
        if yanswer[j] == a:
            score[1] += 1
        j += 1
        if j == 8:
            j = 0

        if zanswer[k] == a:
            score[2] +=1
        k += 1
        if k == 10:
            k = 0

    maxv = max(score)

    if score[0] == maxv and score[1] == maxv and score[2] == maxv:
        return [1,2,3]
    elif score[0] == maxv and score[1] == maxv and score[2] != maxv:
        return [1,2]
    elif score[0] == maxv and score[1] != maxv and score[2] == maxv:
        return [1,3]
    elif score[0] != maxv and score[1] == maxv and score[2] == maxv:
        return [2,3]
    else:
        return [score.index(maxv)+1]

    
    

        
