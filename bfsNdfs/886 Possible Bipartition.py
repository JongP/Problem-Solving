from collections import defaultdict

from collections import defaultdict
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        visited=[-1]*n
        #graph=[[] for _ in range(n)]
        graph=defaultdict(list)
        
        for a,b in dislikes:
            graph[a-1].append(b-1)
            graph[b-1].append(a-1)
        
        def goDFS(node,visited,graph):
            for nextt in graph[node]:
                if visited[nextt]==-1:
                    visited[nextt]=1^visited[node]
                    if not goDFS(nextt,visited,graph):
                        return False
                elif visited[nextt]==visited[node]:
                    return False
            
            return True
        
        
        for i in range(n):
            if visited[i]==-1:
                visited[i]=0
                if not goDFS(i,visited,graph):
                    return False
                
        return True
        
#find sth wrong
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        visited=[-1]*n
        graph=defaultdict(list)
        
        for a,b in dislikes:
            graph[a-1].append(b-1)
            graph[b-1].append(a-1)
        
        def goDFS(node):
            
            for nextt in graph[node]:
                if visited[nextt]==-1:
                    visited[nextt]=~visited[node] #this doesn't work as I thought
                    if not goDFS(nextt):
                        return False
                elif visited[nextt]==visited[node]:
                    return False
            
            
            return True
        
        
        for i in range(n):
            if visited[i]==-1:
                #u forgot sth
                if not goDFS(i):
                    return False
                
        return True
        