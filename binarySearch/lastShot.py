from collections import defaultdict
import bisect

def solution(arr, queries):
    res=[]
    hashMap = defaultdict(list)
    
    for i,v in enumerate(arr):
        hashMap[v].append(i)

    
    for x,y,z in queries:
        total = 0
    
        dp =[0]*len(hashMap[y])
        for i,idx2 in enumerate(hashMap[y]):
            ii3 = bisect.bisect(hashMap[z],idx2)
            dp[i] = len(hashMap[z])-ii3
        
        for i in range(len(dp)-2,-1,-1):
            dp[i]+=dp[i+1]
            
        
        for idx1 in hashMap[x]:
            ii2 = bisect.bisect(hashMap[y],idx1)
            
            if ii2!= len(hashMap[y]):
                total += dp[ii2]

        res.append(total)


    return res

"""   
    res=[]
    hashMap = defaultdict(list)
    
    for i,v in enumerate(arr):
        hashMap[v].append(i)
    
    
    for x,y,z in queries:
        total = 0
        
        for idx1 in hashMap[x]:
            
            i2 = bisect.bisect(hashMap[y],idx1)
            
            if i2 == len(hashMap[y]):
                continue
                
            for ii2 in range(i2,len(hashMap[y])):
                idx2 = hashMap[y][ii2]
                
                i3 = bisect.bisect(hashMap[z],idx2)
                
                total += (len(hashMap[z])-i3)
                
        res.append(total)
                
             
        
    return res
"""