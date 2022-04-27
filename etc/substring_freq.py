import bisect
from collections import defaultdict
def solution(a, queries):
    freqs = defaultdict(list)
    
    
    for i,v in enumerate(a):
        freqs[v].append(i)
        
        
    #queries
    total=0
    
    for l,r,x in queries:
        if x not in freqs:
            continue
            
        leftIdx = bisect.bisect_left(freqs[x],l)
        rightIdx = bisect.bisect(freqs[x],r)
        rightIdx-=1
        
        if leftIdx!= len(freqs[x]) and rightIdx!=-1 and leftIdx<=rightIdx:
            total+= rightIdx-leftIdx+1
        
    
    return total
    
    
    
