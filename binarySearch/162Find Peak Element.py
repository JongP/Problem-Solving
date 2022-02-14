class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l=len(nums)
        le,ri=0,l-1
        
        while le<=ri:
            mid=(le+ri)//2
            
            lVal=nums[mid-1] if 0<mid else -float('inf')
            mVal=nums[mid]
            rVal=nums[mid+1] if mid+1<l else -float('inf')
            
            if lVal<mVal and mVal>rVal: return mid
            elif lVal<mVal<rVal: le=mid+1
            else: ri=mid-1