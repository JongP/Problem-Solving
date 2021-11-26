from functools import reduce
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=len(nums)
        if l==2:
            return nums
        
        ans=[]
        
        #get xor sum
        xSum=reduce(lambda acc,cur:acc^cur,nums)
        
        #find the rightmost different bit
        cnt=0
        tSum=xSum
        while not tSum&1:
            tSum>>=1
            cnt+=1
        
        grainer= 1<<cnt
        
        num1=0
        for num in nums:
            if num&grainer:
                num1^=num
                
        return [num1,num1^xSum]