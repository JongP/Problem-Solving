class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        hashMap=collections.defaultdict(int)
        total=0
        res=0
        
        
        for i,ch in enumerate(s):
            
            total-= hashMap[ch]==1
            hashMap[ch]+=1
            total+= hashMap[ch]==1
                
            if total==k: res+=1
            
            if i>=k-1:
                lChar=s[i-k+1]
                total-= hashMap[lChar]==1
                hashMap[lChar]-=1
                total+= hashMap[lChar]==1

        
        return res
        
#https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/discuss/322928/JavaC%2B%2BPython-Sliding-Window
    def numKLenSubstrNoRepeats(self, S, K):
        res, i = 0, 0
        cur = set()
        for j in xrange(len(S)):
            while S[j] in cur:
                cur.remove(S[i])
                i += 1
            cur.add(S[j])
            res += j - i + 1 >= K
        return res
