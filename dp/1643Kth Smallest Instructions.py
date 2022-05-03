class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        m,n=destination
        graph = self.buildGraph(destination)
        
        path=[]
        
        def findPath(x,y,k,path):
            if (x,y) == (m,n):
                return
            
            hVal = graph[x][y+1] if y!=n else 0
            vVal = graph[x+1][y] if x!=m else 0
            #go H
            if hVal!=0 and hVal>=k:
                path.append("H")
                findPath(x,y+1,k,path)
            #go V
            else:
                path.append("V")
                findPath(x+1,y,k-hVal,path)

        
        findPath(0,0,k,path)
        return "".join(path)
        
        
        
        
    def buildGraph(self,destination):
        m,n=destination
        m+=1
        n+=1
        
        res =[[0]*n for _ in range(m)] 
        res[-1][-1] = 1
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                
                res[i][j] += (res[i][j+1] if j!=n-1 else 0) + (res[i+1][j] if i!=m-1 else 0)
                
        return res
                
                