"""
You are given two arrays of integers a and b, and two integers lower and upper. Your task is to find the number of pairs (i, j) such that lower ≤ a[i] * a[i] + b[j] * b[j] ≤ upper.
"""
import bisect

def solution(a, b, lower, upper):
    a=list(map(lambda x:x**2,a))
    b=list(map(lambda x:x**2,b))
    #print(a,b)
    res=0
    
    if len(b)>len(a):
        a,b=b,a
    
    a.sort()
    #print(a)
    for bVal in b:
        #find  lower - bVal <= aVal <= upper -bVal
        
        leftIdx = bisect.bisect_left(a,lower-bVal)
        rightIdx = bisect.bisect(a,upper-bVal)
        rightIdx-=1
        
        
        if leftIdx==len(a):
            continue
        if rightIdx==-1:
            continue
        #print(bVal,leftIdx,rightIdx)
        
        res+=(rightIdx - leftIdx +1) if rightIdx-leftIdx>=0 else 0
        
    
    
    
    return res