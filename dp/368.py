class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        
        l=len(nums)
        
        if l==1:
            return nums
        
        dp=[1]*l
        bt=[i for i in range(l)]
        
        #initialization
        maxLen=1
        maxIdx=0

        
        for i in range(1,l):
            cur=nums[i]
            for j in range(i):
                if cur%nums[j]==0 and dp[j]+1>dp[i]:
                    dp[i]=dp[j]+1
                    bt[i]=j
                    if maxLen<dp[i]:
                        maxLen=dp[i]
                        maxIdx=i
        idx=maxIdx
        answer=[]
        while True:
            answer.append(nums[idx])
            
            if bt[idx]==idx:
                break
                
            idx=bt[idx]
                
                
        answer.reverse()
        
        return answer
#https://leetcode.com/problems/largest-divisible-subset/discuss/1580106/Python-or-Simple-Solution-With-Detailed-Explaination
    def simpleLargestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        divisibleSubset = [[num] for num in nums]
        
        for i in range(len(nums)):
            for j in range(i):
                if (nums[i] % nums[j]) == 0 and len(divisibleSubset[i]) < len(divisibleSubset[j]) + 1:
                    divisibleSubset[i] = divisibleSubset[j] + [nums[i]]
                    
        return max(divisibleSubset, key=len)