#검증되지 않은 생각이 어떻게 풀이를 망치는가?
#I'm biased in iterative way. you can try reverse

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k==0:
            return
        
        startIdx=0
        cnt=0
        l=len(nums)
        
        while cnt!=len(nums):
            idx=startIdx
            nextValue=nums[(idx+k)%l]
            nums[(idx+k)%l]=nums[idx]
            idx=(idx+k)%l
            cnt+=1
            
            while idx!=startIdx and cnt!=len(nums):
                tmp=nums[(idx+k)%l] 
                nums[(idx+k)%l] = nextValue            
                nextValue=tmp
                cnt+=1
                idx=(idx+k)%l
            
            
            startIdx+=1

#https://leetcode.com/problems/rotate-array/discuss/54426/Summary-of-solutions-in-Python
    def rotate(self, nums, k):
        if k is None or k <= 0:
            return
        k, end = k % len(nums), len(nums) - 1
        self.reverse(nums, 0, end - k)
        self.reverse(nums, end - k + 1, end)
        self.reverse(nums, 0, end)
        
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1


#iterative
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n, k, j = len(nums), k % len(nums), 0
        while n > 0 and k % n != 0:
            for i in xrange(0, k):
                nums[j + i], nums[len(nums) - k + i] = nums[len(nums) - k + i], nums[j + i] # swap
            n, j = n - k, j + k
            k = k % n