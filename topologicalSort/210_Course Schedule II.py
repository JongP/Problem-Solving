from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegrees=[0]*numCourses
        graph=defaultdict(list)
        res=[]
        
        for a,b in prerequisites:
            graph[b].append(a)
            inDegrees[a]+=1
            
        que=[]
        
        for i,v in enumerate(inDegrees):
            if v==0:
                que.append(i)
        
        
        while que:
            cur=que.pop()
            res.append(cur)
            
            for nex in graph[cur]:
                inDegrees[nex]-=1
                if inDegrees[nex]==0:
                    que.append(nex)
                    
                    

        return res if len(res)==numCourses else []
            