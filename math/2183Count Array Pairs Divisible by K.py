#hint: gcd
class Solution:
    #O(n*sqrt(n))
    def countPairs(self, nums: List[int], k: int) -> int:
        hashMap={}
        res=0
        for num in nums:
            num= math.gcd(num,k)
            
            for key,val in hashMap.items():
                if (key*num)%k==0:
                    res+=val
                    
            hashMap[num]=hashMap.get(num,0)+1
            
        return res


#https://leetcode.com/problems/count-array-pairs-divisible-by-k/discuss/1785027/C%2B%2BPython-Easy-and-Concise-with-Explanation
# Time O(nlog100000 + k * k) --> O(n)
# Space O(k)
# where k is the number of divisors of k.
    def coutPairs(self, A, k):
        cnt = Counter(math.gcd(a, k) for a in A)
        res = 0
        for a in cnt:
            for b in cnt:
                if a <= b and a * b % k == 0:
                    res += cnt[a] * cnt[b] if a < b else cnt[a] * (cnt[a] - 1) // 2
        return res

