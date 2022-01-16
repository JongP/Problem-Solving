#unsovled

class Solution:
    #O(n) O(n)
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=set(nums)
        res=1
        while res in nums:res+=1
        return res


#https://leetcode.com/problems/first-missing-positive/discuss/872448/Python-O(n)-solution-with-constant-space-EXPLAINED-with-clear-train-of-thoughts
    def firstMissingPositive(self, nums: List[int]) -> int:
        l=len(nums)
        
        for i in range(l):
            if nums[i]<0 or nums[i]>l:
                nums[i]=0
        
        for i in range(l):
            v=abs(nums[i])
            if v!=0:
                if nums[v-1]==0:
                    nums[v-1]=-1*v
                elif nums[v-1]>0:
                    nums[v-1]*=-1
            
        for i in range(l):
            if nums[i]>=0:
                return i+1
        
        return l+1
            