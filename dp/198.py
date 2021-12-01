class Solution:
    def rob(self, nums: List[int]) -> int:
        l=len(nums)
        
        if l<=2:
            return max(nums)
        
        dp=[0]*l
         
        #initialization
        dp[0]=nums[0]
        dp[1]=nums[1]
        
        #dp[0]
        for i in range(1,l):
            dp[i]=max(dp[i-1],nums[i]+dp[i-2])
        
        
        
        
        return dp[-1]

#sample solution. Space complexity O(1)
    def rob(self, nums: List[int]) -> int:
        prev2_max, prev_max = 0, 0
        
        for n in nums:
            cur = max(prev2_max + n, prev_max)  # max of rob cur house vs not rob cur house
            prev2_max, prev_max = prev_max, cur
        
        return prev_max


#general theory of DP
#https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.