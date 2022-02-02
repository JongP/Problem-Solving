"""
first wrong solution
[1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
2
"""
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        le=0
        ri=len(nums)-1
        
        while le+1<ri:
            mid=(le+ri)//2
            
            if nums[mid]<=nums[ri]:
                if nums[mid]<=target<=nums[ri]:
                    le=mid
                else:
                    ri=mid-1
            else:
                if nums[le]<=target<=nums[mid]:
                    ri=mid
                else:
                    le=mid+1
                    
        return nums[le]==target or nums[ri]==target


#adjusted solution 
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        le=0
        ri=len(nums)-1
        
        while le<=ri:
            mid=(le+ri)//2
            
            if nums[mid]==target: return True
            
            if nums[le]==nums[ri]:
                if nums[le]==target: return True
                le+=1;ri-=1
            elif nums[mid]<=nums[ri]: #[1,1,1,1,1,1,1,1,1,13,1,1,1,1,1,1,1,1,1,1,1,1] 13--> why do I need "=" or [13,1,1,1]
                if nums[mid]<target<=nums[ri]:
                    le=mid+1
                else:
                    ri=mid-1
            else:
                if nums[le]<=target<nums[mid]:
                    ri=mid-1
                else:
                    le=mid+1
                    
        return False



#https://leetcode.com/problems/search-in-rotated-sorted-array-ii/discuss/28195/Python-easy-to-understand-solution-(with-comments).
def search(self, nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
        mid = l + (r-l)//2
        if nums[mid] == target:
            return True
        while l < mid and nums[l] == nums[mid]: # tricky part
            l += 1
        # the first half is ordered
        if nums[l] <= nums[mid]:
            # target is in the first half
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        # the second half is ordered
        else:
            # target is in the second half
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return False