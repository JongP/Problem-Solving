class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        l1,l2=len(nums1),len(nums2)
        
        dp=[[0]*l2 for _ in range(l1)]
        
        for i in range(l1):
            for j in range(l2):
                val = max(nums1[i]*nums2[j] + (dp[i-1][j-1] if i!=0 and j!=0 else 0) ,nums1[i]*nums2[j])
                dp[i][j] = max(dp[i-1][j] if i!=0 else -math.inf,dp[i][j-1] if j!=0 else -math.inf,val)

        
        return dp[-1][-1]

