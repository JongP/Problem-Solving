class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1: return 1
        i=j=2
        
        while j<len(nums):
            if nums[i-2]!=nums[j]:
                nums[i]=nums[j]
                i+=1
            
            j+=1
        
        
        return i
        
        
        