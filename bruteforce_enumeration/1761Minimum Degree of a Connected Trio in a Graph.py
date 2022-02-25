class Solution:
    #O(n^3)
    def buildGraph(self,n,edges):
        graph=[set() for _ in range(n)]
        
        for a,b in edges:
            graph[a-1].add(b-1)
            graph[b-1].add(a-1)
            
        return graph
    
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph=self.buildGraph(n,edges)

        res=math.inf
        
        for i in range(n):
            
            for a in graph[i]:
                if a<i: continue
                for b in graph[i]:
                    if a==b or b<i or b not in graph[a]: continue
                    if len(graph[i])+len(graph[a])+len(graph[b])-6<res:
                        res=len(graph[i])+len(graph[a])+len(graph[b])-6
                              
            
        return res==math.inf and -1 or res


#just reduced repetition
class Solution:
    
    def buildGraph(self,n,edges):
        graph=[set() for _ in range(n)]
        
        for a,b in edges:
            graph[a-1].add(b-1)
            graph[b-1].add(a-1)
            
        return graph
    
    def buildList(self,n,edges):
        graph=[[] for _ in range(n)]
        
        for a,b in edges:
            if a>b:
                a,b=b,a
            graph[a-1].append(b-1)
            
        return graph
            
        
    
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph=self.buildGraph(n,edges)
        listGraph=self.buildList(n,edges)
        
        res=math.inf
        
        for i in range(n):
            
            for j in range(len(listGraph[i])):
                a=listGraph[i][j]
                for k in range(j+1,len(listGraph[i])):
                    b= listGraph[i][k]
                    
                    if b not in graph[a]: continue
                    if len(graph[i])+len(graph[a])+len(graph[b])-6<res:
                        res=len(graph[i])+len(graph[a])+len(graph[b])-6
                    
  
        return res==math.inf and -1 or res
        

#https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/discuss/1064616/Python-3-simple-brute-force-solution
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        g = collections.defaultdict(set)
        for (a,b) in edges:
            g[a].add(b)
            g[b].add(a)
            
        d = collections.defaultdict(int)
        for n in g:
            d[n] = len(g[n])
            
        res = float('inf')
        for n in g:
            for m in g[n]:
                for o in g[n] & g[m]:
                    res = min(res, d[n]+d[m]+d[o]-6)
                    if n in g[o]:
                        g[o].remove(n)
                if n in g[m]:
                    g[m].remove(n)
        if res == float('inf'):
            return -1
        else:
            return res