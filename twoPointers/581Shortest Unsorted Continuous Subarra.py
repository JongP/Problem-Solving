#struggled in special cases

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums=[-1*math.inf]+nums+[math.inf]
        le=0
        ri=len(nums)-1
        mid=1
        
        while mid<len(nums) and nums[mid-1]<=nums[mid]: mid+=1
        if mid==len(nums): return 0
        
        while ri>=0 and nums[ri-1]<=nums[ri]:ri-=1
        #print(nums,mid,ri)
        
        minV=maxV=nums[mid]
        for i in range(mid-1,ri+1):#important
            if minV>nums[i]:minV=nums[i]
            if maxV<nums[i]:maxV=nums[i]
        
        
        while mid>0 and nums[mid-1]>minV: mid-=1
        while ri<len(nums) and nums[ri]<maxV: ri+=1
        
        return ri-mid


#https://leetcode.com/problems/shortest-unsorted-continuous-subarray/discuss/1082092/Python-Short-O(n)-solution-explained
#prefixMax, surfixMin
class Solution:
    def findUnsortedSubarray(self, nums):
        nums = [-float("inf")] + nums + [float("inf")]
        run_max = list(accumulate(nums, max))
        run_min = list(accumulate(nums[::-1], min))[::-1]
        
        end, beg = len(nums) - 1, 0

        while nums[end-1] <= nums[end] and run_max[end-1] <= nums[end - 1]:
            end -= 1
            
        if end == 0: return 0
            
        while nums[beg+1] >= nums[beg] and run_min[beg+1] >= nums[beg + 1]:
            beg += 1
            
        return end - beg - 1

"""
What is the end pointer? It is the smallest value such that

max(nums[0], nums[1], ..., nums[end]) <= nums[end + 1] <= nums[end + 2] <= ... <= nums[-1]:
"""