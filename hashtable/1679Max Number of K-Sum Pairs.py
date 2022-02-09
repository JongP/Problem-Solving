from collections import defaultdict
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hashTable=defaultdict(int)
        res=0
        for num in nums:
            if hashTable[k-num]>0:
                res+=1
                hashTable[k-num]-=1
            else: 
                hashTable[num]+=1
        return res

#https://leetcode.com/problems/max-number-of-k-sum-pairs/discuss/1022699/Python-Short-Counter-solution-%2B-Oneliner-explained
class Solution:
    def maxOperations(self, nums, k):
        cnt, ans = Counter(nums), 0
        for val in cnt:
            ans += min(cnt[val], cnt[k - val])
        return ans//2