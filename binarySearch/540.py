#Single Element in a Sorted Array
class Solution:
    def singleNonDuplicate(self, nums) -> int:
        #len() take cost 1
        le=0
        ri=(len(nums)-3)//2

        
        #corner case
        if len(nums)==1:
            return nums[0]
        if nums[-1]!=nums[-2]:
            return nums[-1]

        while le<ri:
            mid=(le+ri)//2
            
            if nums[2*mid]==nums[2*mid+1]:
                le=mid+1
            else:
                ri=mid

        return nums[2*ri]

#failed to come up with binarySearch. But log(n) implies binary search

sol=Solution()
print(sol.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))