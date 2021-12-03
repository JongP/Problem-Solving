class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l=len(nums)
        ans=max(nums)
        
        dp=nums.copy()
        
        if nums[0]<0:
            lm=0
        else:
            lm=-1   
        
        for i in range(1,l):
            v=nums[i]
            
            if v<0 and lm==-1:
                lm=i
            
            if dp[i-1]==0:
                continue
                
            if v==0:
                if lm!=-1 and lm!=i-1:
                    ans=max(ans,dp[i-1]//dp[lm])
                lm=-1
                continue
            
            dp[i]=dp[i-1]*v
            ans=max(ans,dp[i])
            
        if lm!=-1 and lm!=l-1:
                ans=max(ans,dp[l-1]//dp[lm])  
    
        print(dp,lm)
        return ans

#https://leetcode.com/problems/maximum-product-subarray/discuss/183483/JavaC%2B%2BPython-it-can-be-more-simple
    def maxProduct(self, A):
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(A + B)
#https://leetcode.com/problems/maximum-product-subarray/discuss/384555/Python-Solution-(DP)
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        min_so_far, max_so_far, max_global = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            max_so_far, min_so_far = max(min_so_far*nums[i], max_so_far*nums[i], nums[i]), min(min_so_far*nums[i], max_so_far*nums[i], nums[i])
            max_global = max(max_global, max_so_far)
        
        return max_global