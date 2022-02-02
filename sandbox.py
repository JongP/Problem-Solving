class Solution:
    def search(self, nums, target) :
        le=0
        ri=len(nums)-1
        
        while le<=ri:
            mid=(le+ri)//2
            print(mid,nums[le:ri+1],nums[mid])
            if nums[mid]==target: return True
            
            if nums[le]==nums[ri]:
                if nums[le]==target: return True
                le+=1;ri-=1
            elif nums[mid]<nums[ri]:
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
sol=Solution()
print(sol.search([1,1,1,1,1,1,1,1,1,13,1,1,1,1,1,1,1,1,1,1,1,1],13))
