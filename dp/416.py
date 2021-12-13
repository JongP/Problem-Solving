class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        l=len(nums)
        target,mod=divmod(sum(nums),2)
        
        if mod!=0:
            return False
        
        dp=[0]*(target+1)
        dp[0]=1
        
        #print(target)
        
        for i in range(1,l+1):
            num=nums[i-1]
            prevDP=dp.copy()
            for j in range(target+1):
                if prevDP[j]==1 and j+num<target+1:
                    #print(j,num)
                    dp[j+num]=1
                    if j+num==target:
                        return True
                        
        return False

#hint w/ topic(kanpsack)

#wrong
#at [1,2,5], dp calculated in modified 
    def canPartition(self, nums: List[int]) -> bool:
        l=len(nums)
        target,mod=divmod(sum(nums),2)
        
        if mod!=0:
            return False
        
        dp=[0]*(target+1)
        dp[0]=1
        
        
        for i in range(1,l+1):
            num=nums[i-1]
            for j in range(target+1):
                if dp[j]==1 and j+num<target+1:
                    dp[j+num]=1
                    if j+num==target:
                        return True
                    
                
        
        
        return False


#https://leetcode.com/problems/partition-equal-subset-sum/discuss/276278/Python-DP-and-(DFS%2BMemo)
def canPartition(nums):
	s, n, memo = sum(nums), len(nums), {0: True}
        if s & 1: return False
        nums.sort(reverse=True)
        def dfs(i, x):
            if x not in memo:
                memo[x] = False
                if x > 0:
                    for j in range(i, n):
                        if dfs(j+1, x-nums[j]):
                            memo[x] = True
                            break
            return memo[x]
        return dfs(0, s >> 1)