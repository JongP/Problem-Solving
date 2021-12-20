class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res=[]

        def helper(idx,cur,s):
            
            if s==target:
                self.res.append(cur[:])
                return
            
            if idx>=len(candidates) or s>target:
                return
            
            cur.append(candidates[idx])
            helper(idx,cur,s+candidates[idx])
            cur.pop()
            helper(idx+1,cur,s)
            
            
        
        helper(0,[],0)
        
        return self.res