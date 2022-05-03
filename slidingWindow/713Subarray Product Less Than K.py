class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        le=ri=0
        total=nums[0]
        l=len(nums)
        cnt=0
        
        while le<l:
            
            if ri<le:
                ri=le
                total=nums[le]
            
            while ri+1<l and total*nums[ri+1]<k:
                total*=nums[ri+1]
                ri+=1
            
            if total<k:
                cnt+=(ri-le+1)
                #print(le,ri)
            
            
            total//=nums[le]
            le+=1
            
        return cnt

#leetcode
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans