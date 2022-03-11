class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp={}
        surfixSum=self.getSurfixSum(nums)
        
        
        def dfs(idx,target):
            if idx==len(nums):
                if target==0:
                    return 1
                return 0
            
            
            if (idx,target) in dp:
                return dp[(idx,target)]
            
            
            if abs(target)>surfixSum[idx]:
                dp[(idx,target)]=0
                return 0
#             elif abs(target)==abs(surfixSum[idx]) and target!=0:
#                 dp[(idx,target)]=1
#                 return 1
            
            
            dp[(idx,target)] = dfs(idx+1,target+nums[idx]) + dfs(idx+1,target-nums[idx])
            
            return dp[(idx,target)]
            
            
        return dfs(0,target)
        
        
        
    
    def getSurfixSum(self,nums):
        n=len(nums)
        res=[0]*n
        res[-1]=abs(nums[-1])
        
        for i in range(n-2,-1,-1):
            res[i]=res[i+1]+abs(nums[i])
        
        return res


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp={}
        surfixSum,surfixZero=self.getSurfixSum(nums)
        print(surfixZero)
        
        def dfs(idx,target):
            if idx==len(nums):
                if target==0:
                    return 1
                return 0
            
            
            if (idx,target) in dp:
                return dp[(idx,target)]
            
            
            if abs(target)>surfixSum[idx]:
                dp[(idx,target)]=0
                return 0
            elif abs(target)==abs(surfixSum[idx]):
                dp[(idx,target)]= 1<<surfixZero[idx]
                return dp[(idx,target)]
           
            
            dp[(idx,target)] = dfs(idx+1,target+nums[idx]) + dfs(idx+1,target-nums[idx])
            
            return dp[(idx,target)]
            
        return dfs(0,target)
        
        
        
    
    def getSurfixSum(self,nums):
        n=len(nums)
        res=[0]*n
        res2=[0]*n
    
        res[-1]=abs(nums[-1])
        res2[-1]= 1 if nums[-1]==0 else 0
        
        for i in range(n-2,-1,-1):
            res[i]=res[i+1]+abs(nums[i])
            
            res2[i]=res2[i+1]+ (nums[i]==0)
        
        return res,res2
        
#https://leetcode.com/problems/target-sum/discuss/97439/JavaPython-Easily-Understood
    def findTargetSumWays(self, A, S):
        count = collections.Counter({0: 1})
        for x in A:
            step = collections.Counter()
            for y in count:
                step[y + x] += count[y]
                step[y - x] += count[y]
            count = step
        return count[S]


#https://leetcode.com/problems/target-sum/discuss/455024/DP-IS-EASY!-5-Steps-to-Think-Through-DP-Questions.
class Solution:
    def findTargetSumWays(self, nums, S):
        index = len(nums) - 1
        curr_sum = 0
        self.memo = {}
        return self.dp(nums, S, index, curr_sum)
        
    def dp(self, nums, target, index, curr_sum):
        if (index, curr_sum) in self.memo:
            return self.memo[(index, curr_sum)]
        
        if index < 0 and curr_sum == target:
            return 1
        if index < 0:
            return 0 
        
        positive = self.dp(nums, target, index-1, curr_sum + nums[index])
        negative = self.dp(nums, target, index-1, curr_sum + -nums[index])
        
        self.memo[(index, curr_sum)] = positive + negative
        return self.memo[(index, curr_sum)]
"""
Question: Identify this problem as one of the categories below before continuing.

0/1 Knapsack
Unbounded Knapsack
Shortest Path (eg: Unique Paths I/II)
Fibonacci Sequence (eg: House Thief, Jump Game)
Longest Common Substring/Subsequeunce
"""