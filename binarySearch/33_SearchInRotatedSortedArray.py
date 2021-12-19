class Solution:
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