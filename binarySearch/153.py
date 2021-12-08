class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=len(nums)
        minN=nums[0]
        maxN=nums[-1]
        
        #l==1 or rotated n times
        if l==1 or minN<maxN:
            return nums[0]
        
        le=0
        ri=l-1
        
        while le<ri:
            mid=(le+ri)//2
            #print(nums[mid])
            if nums[mid]>=minN:
                le=mid+1
            else:
                ri=mid
        
        return nums[le]

#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/48749/My-binary-search-solution-in-Python-with-disscussing
    def findMin(self, num):
        first, last = 0, len(num) - 1
        while first < last:
            midpoint = (first + last) // 2
            if num[midpoint] > num[last]:
                first = midpoint + 1
            else:
                last = midpoint
        return num[first]