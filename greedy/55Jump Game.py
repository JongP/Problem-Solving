class Solution(object):
    def canJump(self, nums):
        if nums[0]+1>=len(nums): return True
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        maxReach=tmpReach=nums[0]
        
        for i,v in enumerate(nums):
            if tmpReach<i+v:
                tmpReach=i+v
            
            if i==maxReach:
                maxReach=tmpReach
                if maxReach>=len(nums)-1: return True

            
        return False
        