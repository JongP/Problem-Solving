from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        ans=[]
        cnt=n
        inDegrees=[0]*n
        graph=[[] for _ in range(n)]
        
        if n<=2:
            return [i for i in range(n)]
        
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            inDegrees[a]+=1
            inDegrees[b]+=1

        lst= deque([i for i in range(n) if inDegrees[i]==1])
        while lst:
            l=len(lst)
            cnt-=l
            if cnt<=2:
                break
            
            for _ in range(l):
                cur=lst.popleft()
                
                for nxt in graph[cur]:
                    if inDegrees[nxt]==1:
                        continue
                    
                    inDegrees[nxt]-=1
                    if inDegrees[nxt]==1:
                        lst.append(nxt)
        
        for i,v in enumerate(inDegrees):
            if v!=1:
                ans.append(i)
                cnt-=1
                if cnt==0:
                    break
        
            
        return ans

#hint: We are basically trying to delete all leaf nodes at every step. This is very similar to Kahn's Algo or sometimes known as BFS Topological Sort.
#https://leetcode.com/problems/minimum-height-trees/discuss/1247810/C%2B%2B-Kahn's-Algo-(BFS-Topo-Sort)-Solution