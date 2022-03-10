#sovled with two hint
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        l=len(nums)
        prev=-math.inf
        res=-math.inf
        
        prefixSum=[0]*l;prefixSum[0]=nums[0]
        surfixSum=[0]*l;surfixSum[-1]=nums[-1]
        
        for i in range(len(nums)):
            j=l-1-i
            
            #kadane
            prev=max(prev+nums[i],nums[i])
            if prev>res:res=prev
            #prefixSum
            if i!=0:
                prefixSum[i]=prefixSum[i-1]+nums[i]
            
            #surfixSum
                surfixSum[j]=surfixSum[j+1]+nums[j]
                
        for i in range(1,len(nums)):
            j=l-1-i
            
            prefixSum[i]=max(prefixSum[i],prefixSum[i-1])
            surfixSum[j]=max(surfixSum[j],surfixSum[j+1])
            
        
        for i in range(len(nums)-1):
            res=max(res,prefixSum[i]+surfixSum[i+1])
                
            
        return res

#min subarray
#https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/178422/One-Pass
    def maxSubarraySumCircular(self, A):
        total, maxSum, curMax, minSum, curMin = 0, A[0], 0, A[0], 0
        for a in A:
            curMax = max(curMax + a, a)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + a, a)
            minSum = min(minSum, curMin)
            total += a
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum