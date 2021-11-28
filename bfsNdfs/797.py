class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans=[]
        l=len(graph)
        target=l-1
        
        def goDFS(idx,stk):
            stk.append(idx)
            if idx==target:
                ans.append(stk[:])#cant reference to stk
                return
        
            for nIdx in graph[idx]:
                goDFS(nIdx,stk)
                stk.pop() #don't have to make new stk
            
        goDFS(0,[])
        
        return ans