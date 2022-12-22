def solution(array, commands):
    
    ans = []
    for arr in commands:
    	rsutarr = array[arr[0]-1:arr[1]]
    	rsutarr.sort()
    	ans.append(rsutarr[arr[2]-1])
    return ans