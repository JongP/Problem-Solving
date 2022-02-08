class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1: return 0
        maxReach=nums[0]
        res=1
        idx=0
        while maxReach<len(nums)-1:
            tmpReach=maxReach
            while idx<=maxReach:
                if tmpReach<idx+nums[idx]:
                    tmpReach=idx+nums[idx]
                idx+=1
            maxReach=tmpReach
            res+=1
        
        
        
        return res