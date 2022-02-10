class Solution:
    #O(N)
    #function consume time quite a lot
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def myReverse(nums,idx):
            le=idx
            ri=len(nums)-1
            
            while le<ri:
                nums[le],nums[ri]=nums[ri],nums[le]
                le+=1
                ri-=1
            
        
        idx=len(nums)-1
        while idx>0 and nums[idx-1]>=nums[idx]:idx-=1
        if idx==0: 
            myReverse(nums,0)
            return
        
        val=nums[idx-1]
        cIdx=len(nums)-1
        while nums[cIdx]<=val:cIdx-=1
        nums[cIdx],nums[idx-1]=nums[idx-1],nums[cIdx]
        
        myReverse(nums,idx)



#https://leetcode.com/problems/next-permutation/discuss/229211/Python-solution
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i-1]:
                j = i
                while j < n and nums[j] > nums[i-1]:
                    idx = j
                    j += 1
                nums[idx], nums[i-1] = nums[i-1], nums[idx]
                for k in range((n-i)//2):
                    nums[i+k], nums[n-1-k] = nums[n-1-k], nums[i+k]
                break
        else:
            nums.reverse()