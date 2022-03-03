class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        l=len(nums)
        if l<=2: return 0
        
        idx1,idx2=0,1
        
        res=0
        
        while idx1<l-2:
            diff=nums[idx1]-nums[idx2]
            
            while idx2+1<l and nums[idx2]-nums[idx2+1]==diff: idx2+=1
                
            if idx2-idx1>=2:
                res+= (idx2-idx1)*(idx2-idx1-1)//2  
            
            idx1=idx2
            idx2=idx1+1

            
            
        return res

#https://leetcode.com/problems/arithmetic-slices/discuss/1455367/Python-Bottom-up-DP-Time-O(N)-Space-O(1)-Clean-and-Concise
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        ans = 0
        for i in range(2, n):
            if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                dp[i] = dp[i-1] + 1
            ans += dp[i]
        return ans