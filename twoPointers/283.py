class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zIdx=-1
        for i in range(len(nums)):
            if nums[i]==0:
                zIdx=i
                break
        
        if zIdx==-1:
            return
        
        
        idx=0
        while idx<len(nums):
            
            if zIdx<idx and nums[idx]!=0:
                nums[zIdx]=nums[idx]
                nums[idx]=0
                while zIdx<len(nums):
                    if nums[zIdx]==0:
                        break
                    zIdx+=1
            
            idx+=1
    def moveZeroesBest(self, nums):
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1