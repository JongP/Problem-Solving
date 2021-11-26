#https://leetcode.com/problems/maximum-subarray/
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        if l==1:
            return nums[0]
        dp=[0]*l#0th:
        dp[0]=nums[0]
        maxNum=dp[0]
        for i in range(1,l):
            dp[i]=max(nums[i],nums[i]+dp[i-1])
            if maxNum<dp[i]:
                maxNum=dp[i]
            
        return maxNum