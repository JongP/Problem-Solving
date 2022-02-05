from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashMap=defaultdict(int)
        hashMap[0]=1;hashMap[nums[0]]+=1
        
        res=0 if nums[0]!=k else 1
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
            res+=hashMap[nums[i]-k]
            hashMap[nums[i]]+=1
        
        
        print(nums)
        return res
        
#https://leetcode.com/problems/subarray-sum-equals-k/discuss/341399/Python-clear-explanation-with-code-and-example
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        sums = 0
        d = dict()
        d[0] = 1
        
        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums-k,0)
            d[sums] = d.get(sums,0) + 1
        
        return(count)