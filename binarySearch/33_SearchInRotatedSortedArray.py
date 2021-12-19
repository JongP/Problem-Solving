class Solution:
    #clean code
    def search(self, nums: List[int], target: int) -> int:
        l=len(nums)
        t=target
        
        if l==1:
            return 0 if nums[0]==target else -1
        
        le=0
        ri=l-1
        
        while le<=ri:
            mid=(le+ri)//2
            if t<nums[mid] and t<nums[le] and nums[mid]>=nums[le]:
                le=mid+1
            elif t>nums[mid] and t>nums[ri] and nums[mid]<nums[ri] :
                ri=mid-1
            elif t<nums[mid]:
                ri=mid-1
            elif t>nums[mid]:
                le=mid+1
            else:
                return mid

        return -1

    #initial solution
    def search(self, nums: List[int], target: int) -> int:
        l=len(nums)
        t=target
        
        if l==1:
            return 0 if nums[0]==target else -1
        
        le=0
        ri=l-1
        
        while le<=ri:
            mid=(le+ri)//2
            #print(le,ri,mid,nums[mid])
            if t<nums[mid] and t<nums[le]:
                #whetehr nums[mid] belongs to left side or right side
                if nums[mid]>=nums[le]: #[2,1] to detect 1, "=" is required
                    le=mid+1
                else:
                    ri=mid-1
            elif t>nums[mid] and t>nums[ri] :
                if nums[mid]<nums[ri]:
                    ri=mid-1
                else:
                    le=mid+1
            elif t<nums[mid]:
                ri=mid-1
            elif t>nums[mid]:
                le=mid+1
            else:
                return mid
            
            
        return -1
#https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/894031/Python-O(logn)-Detailed-Explanation
    def search(self, A: List[int], target: int) -> int:
        n = len(A)
        left, right = 0, n - 1
        if n == 0: return -1
        
        while left <= right:
            mid = left + (right - left) // 2
            if A[mid] == target: return mid
            
            # inflection point to the right. Left is strictly increasing
            if A[mid] >= A[left]:
                if A[left] <= target < A[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            # inflection point to the left of me. Right is strictly increasing
            else:
                if A[mid] < target <= A[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1