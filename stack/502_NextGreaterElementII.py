class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        l=len(nums)
        stk=[]
        res=[0]*l
        maxNum=max(nums)
        
        
        for idx in range(l):
            while stk and nums[stk[-1]]<nums[idx]:
                res[stk.pop()]=nums[idx]
            if nums[idx]==maxNum:
                res[idx]=-1
            stk.append(idx)
            
        for idx in range(l):
            while stk and nums[stk[-1]]<nums[idx]:
                res[stk.pop()]=nums[idx]
            
            if nums[idx]==maxNum:
                break
        
        
        
        return res
        