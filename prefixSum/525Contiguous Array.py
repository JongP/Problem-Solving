from collections import defaultdict 
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic= {}
        dic[0]=-1
        
        oneMinusZeros=0
        res=0
        for i in range(len(nums)):
            if nums[i]==1: oneMinusZeros+=1
            else: oneMinusZeros-=1
            
            if oneMinusZeros not in dic:
                dic[oneMinusZeros]=i
            
            elif res< i - dic[oneMinusZeros]:
                res=i-dic[oneMinusZeros]
            
        
        return res