from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)==1: return 1
        
        def getVerticalMax(points):
            hashMap={}
            for p in points:
                if p[0] not in hashMap:
                    hashMap[p[0]]=0
                hashMap[p[0]]+=1
            return max(hashMap.values())
        
        
        res=getVerticalMax(points)
        
        
        
        hashMap=defaultdict(int)
        for x1,y1 in points:
            visited=set()
            for x2,y2 in points:
                if x1==x2:continue
                
                a=(y2-y1)/(x2-x1)
                b=y1-a*x1
                print(a,b)
                if (a,b) in visited: continue
                
                visited.add((a,b))
                hashMap[(a,b)]+=1
                
        
        
        
        
        return max(res,max(hashMap.values()) if hashMap else 0 )