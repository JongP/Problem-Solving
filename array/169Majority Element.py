class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        cnter=collections.Counter(nums)
        for i in cnter:
            if cnter[i]>= math.ceil(n/2):
                return i

#Boyer Moore voting algorithm
    def majorityElement(self, nums: List[int]) -> int:
        count,majority=0,nums[0]
        for item in nums:
            if count==0:
                majority=item
                count+=1
            elif majority==item: count+=1
            else: count-=1
        return majority
#https://www.youtube.com/watch?v=7pnhv842keE