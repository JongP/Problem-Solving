class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        visited=[0]*len(nums)
        res=[]
        def backtracing(nums,ans,visited,res):
            if len(ans)==len(nums):
                res.append(ans.copy())
                return 
            
            
            for i in range(len(nums)):
                if visited[i]: continue
                visited[i]=1
                ans.append(nums[i])
                backtracing(nums,ans,visited,res)
                ans.pop()
                visited[i]=0
        
        backtracing(nums,[],visited,res)
        
        return res