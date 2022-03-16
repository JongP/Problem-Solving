class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        
        visited=set()
        
        def dfs(cur):
            visited.add(cur)
            
            for nxt in range(n):
                if isConnected[cur][nxt] and  nxt not in visited:
                    dfs(nxt)
                    
                    
        res=0
        for i in range(n):
            if i not in visited:
                res+=1
                dfs(i)
                
        return res
            
            
            