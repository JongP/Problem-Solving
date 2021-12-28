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

#https://leetcode.com/problems/combination-sum/discuss/16510/Python-dfs-solution.
class Solution(object):
    def combinationSum(self, candidates, target):
        ret = []
        self.dfs(candidates, target, [], ret)
        return ret
    
    def dfs(self, nums, target, path, ret):
        if target < 0:
            return 
        if target == 0:
            ret.append(path)
            return 
        for i in range(len(nums)):
            self.dfs(nums[i:], target-nums[i], path+[nums[i]], ret)


#https://leetcode.com/problems/combination-sum/discuss/751353/Python-92-Faster-97-Space
    def backtrack(self, candidates, target, r, s, i):        
        if s == target:
            self.res.append(r[:])
        
        for j in range(i, len(candidates)):
            c = candidates[j]
            if s + c > target: break
                
            # Place
            r.append(c)
            s += c
            # Search
            self.backtrack(candidates, target, r, s, j)
            
            # Backtrack
            r.pop()
            s -= c
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = list()
        self.backtrack(sorted(candidates), target, [], 0, 0)
        return self.res