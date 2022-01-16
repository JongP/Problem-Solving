import copy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        
        
        def resolver(path):
            tmp=[]
            for i in path:
                tmp.append("."*i+"Q"+"."*(n-i-1))
            res.append(tmp)
            
        def helper(path):
            if len(path)==n:
                resolver(path)
                return
            
            visited=set()
            level=len(path)
            for i in range(len(path)):
                visited.add(path[i])
                if path[i]+level-i <n:
                    visited.add(path[i]+level-i)
                if path[i]-(level-i)>=0:
                    visited.add(path[i]-(level-i))
                
            
            for i in range(n):
                if i in visited: continue
                path.append(i)
                helper(path)
                path.pop()    
            
        helper([])
            
            
        return res

#https://leetcode.com/problems/n-queens/discuss/19810/Fast-short-and-easy-to-understand-python-solution-11-lines-76ms
    def DFS(queens, xy_dif, xy_sum):
        p = len(queens)
        if p==n:
            result.append(queens)
            return None
        for q in range(n):
            if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
    result = []
    DFS([],[],[])
    return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]