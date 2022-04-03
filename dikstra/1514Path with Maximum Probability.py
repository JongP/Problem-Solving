from heapq import heappop, heappush
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        heap=[(-1,start)]
        visited=set()
        
        graph=self.buildGraph(edges,succProb)
        
        while heap:
            prob,node=heappop(heap);
            
            
            if node==end:
                return -prob
            
            if node in visited:
                continue    
            visited.add(node)
            
            for nxt in graph[node]:
                if nxt not in visited:
                    heappush(heap,(prob*graph[node][nxt]  ,nxt  ))
            
            
            
            
            
        return 0
        
    
    def buildGraph(self,edges,succProb):
        graph=collections.defaultdict(dict)
        
        for (a,b), p in zip(edges,succProb):
            if b not in  graph[a] or p>graph[a][b]:
                graph[a][b]=p
            
            if a not in graph[b] or p>graph[b][a]:
                graph[b][a]=p
                
        return graph