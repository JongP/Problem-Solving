class Solution:
    #O(n)
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreaters={}
        stk=[]
        
        for i in range(len(nums2)-1,-1,-1):
            while stk and stk[-1]<=nums2[i]:
                stk.pop()
            
            if stk:
                nextGreaters[nums2[i]]=stk[-1]
            
            stk.append(nums2[i])
            
        return [nextGreaters.get(num1,-1)  for num1 in nums1]