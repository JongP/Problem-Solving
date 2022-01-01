#Matrix Chain Multiplication
#[출처] 알고리즘) Matrix Chain Multiplication|작성자 바보



#https://leetcode.com/problems/burst-balloons/discuss/76228/Share-some-analysis-and-explanations
def maxCoins(self, iNums):
    nums = [1] + [i for i in iNums if i > 0] + [1]
    n = len(nums)
    dp = [[0]*n for _ in xrange(n)]

    for k in xrange(2, n):
        for left in xrange(0, n - k):
            right = left + k
            for i in xrange(left + 1,right):
                dp[left][right] = max(dp[left][right],
                       nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
    return dp[0][n - 1]

#first trial(not solution)
class Solution:
    memo={}
    
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        if tuple(nums) in self.memo:
            return self.memo[tuple(nums)]
        
        tmpMax=0
        for i in range(len(nums)):
            tmpRes=self.maxCoins(nums[:i]+nums[i+1:])
            tmp=nums[i]
            if i>0:
                tmp*=nums[i-1]
            if i<len(nums)-1:
                tmp*=nums[i+1]
            if tmpMax<tmpRes+tmp:
                tmpMax=tmpRes+tmp
        
        self.memo[tuple(nums)]=tmpMax
        
        return tmpMax