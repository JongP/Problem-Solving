#Wiggle Sort

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        for i in range(0,len(nums),2):
            
            lVal= nums[i-1] if i!=0 else -math.inf
            mVal=nums[i]
            rVal=nums[i+1] if i!=len(nums)-1 else -math.inf
            
            
            if lVal>mVal and lVal>rVal:
                nums[i],nums[i-1]=nums[i-1],nums[i]
            elif rVal>mVal and rVal>lVal:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        
        return nums