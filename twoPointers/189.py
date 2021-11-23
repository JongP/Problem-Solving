#189. rotate array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k==0:
            return
        
        startIdx=0
        cnt=0
        l=len(nums)
        
        while cnt!=len(nums):
            idx=startIdx
            nextValue=nums[(idx+k)%l]
            nums[(idx+k)%l]=nums[idx]
            idx=(idx+k)%l
            cnt+=1
            
            while idx!=startIdx and cnt!=len(nums):
                tmp=nums[(idx+k)%l] 
                nums[(idx+k)%l] = nextValue            
                nextValue=tmp
                cnt+=1
                idx=(idx+k)%l
            
            
            startIdx+=1