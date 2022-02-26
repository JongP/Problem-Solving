class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx1=idx2=1
        
        while idx1<len(nums):
            if  nums[idx1]!=nums[idx2-1]:
                nums[idx1],nums[idx2]=nums[idx2],nums[idx1]
                idx2+=1
                

            idx1+=1
        
        return idx2