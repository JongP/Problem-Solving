class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans=[]
        
        def helper(n,idx,cand,k):
            if k==0:
                self.ans.append(cand[:])
                return
            if n<idx:
                return
                
            
            
            
            helper(n,idx+1,cand,k)
            cand.append(idx)
            helper(n,idx+1,cand,k-1)
            cand.pop()
            

        
        helper(n,1,[],k)
        
        return self.ans
#https://leetcode.com/problems/combinations/discuss/26990/Python-easy-to-understand-DFS-solution
    def combine(self, n, k):
        ret = []
        self.dfs(list(range(1, n+1)), k, [], ret)
        return ret
    
    def dfs(self, nums, k, path, ret):
        if len(path) == k:
            ret.append(path)
            return 
        for i in range(len(nums)):
            self.dfs(nums[i+1:], k, path+[nums[i]], ret)