class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res=[]
        l=len(nums)
        
        idx1=idx2=0
        
        while idx1 < l :
            
            while idx2<l-1 and nums[idx2+1] == nums[idx1]+idx2+1-idx1  : idx2+=1
            
            
            if idx1==idx2:
                res.append(str(nums[idx1]))
            else:
                res.append("%d->%d"%(nums[idx1],nums[idx2]))
            
            
            idx1=idx2+1
            
            
        
        return res