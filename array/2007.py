from collections import defaultdict
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        l=len(changed)
        if l&1:
            return None
        changed.sort()
        
        ans=[]
        
        dic=defaultdict(int)
        
        for num in changed:
            dic[num]+=1
        
        for num in changed:
            if not dic[num]: continue
            if dic[num]>dic[num*2]:
                return None
            if num!=0:
                ans+=[num]*dic[num]
            elif dic[0]&1:
                return None
            else:
                ans+=[0]*(dic[num]//2)
            
            dic[num*2]-=dic[num]
            dic[num]=0
        
        if dic[changed[-1]]!=0:
            return None
            
        return ans
#https://leetcode.com/problems/find-original-array-from-doubled-array/discuss/1470959/JavaC%2B%2BPython-Match-from-the-Smallest-or-Biggest-100
# by sorting Counter --> we can reduce time complexity from O(nlogn) to O(n+klogk) where k is number of diff digits.    
    def findOriginalArray(self, A):
        c = collections.Counter(A)
        if c[0] % 2:
            return []
        for x in sorted(c):
            if c[x] > c[2 * x]:
                return []
            c[2 * x] -= c[x] if x else c[x] / 2
        return list(c.elements())