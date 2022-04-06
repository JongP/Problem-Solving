from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sortedList=SortedList()
        
        l=len(nums)
        res=[0]*l
        
        for i in range(l-1,-1,-1):
            idx=sortedList.bisect_left(nums[i])
            idx-=1
            
            if idx!=-1:
                res[i]=idx+1
            
            sortedList.add(nums[i])
            
            
        
        return res


#https://leetcode.com/problems/count-of-smaller-numbers-after-self/solution/
