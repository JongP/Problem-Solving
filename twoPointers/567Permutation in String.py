from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c=Counter(s1)
        cnt=len(c)
        
        
        
        for ri in range(len(s2)):
            #ri
            rC=s2[ri]
            if rC in c:
                if c[rC]==0: cnt+=1
                c[rC]-=1
                if c[rC]==0: cnt-=1
            
            #validate
            if cnt==0: return True
            
            
            #le
            le=ri-len(s1)+1
            if le>=0 and s2[le] in c:
                lC=s2[le]
                if c[lC]==0: cnt+=1
                c[lC]+=1
                if c[lC]==0: cnt-=1
        
        
        return False

from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c=Counter(s1)
        cnt=len(c)
        
        
        def myCounter(s2,idx,c,cnt,isRight):
            if idx<0 or s2[idx] not in c: return cnt
            
            char=s2[idx]
            if c[char]==0: cnt+=1
            c[char]+= (-1 if isRight else 1)
            if c[char]==0: cnt-=1
            
            return cnt
        
        for ri in range(len(s2)):
            #ri
            cnt=myCounter(s2,ri,c,cnt,True)

            #validate
            if cnt==0: return True
            
            #le
            cnt=myCounter(s2,ri-len(s1)+1,c,cnt,False)        
        
        return False

#don't forget leveraging of the number of alphabet
#https://leetcode.com/problems/permutation-in-string/discuss/102594/Python-Simple-with-Explanation
    def checkInclusion(self, s1, s2):
        A = [ord(x) - ord('a') for x in s1]
        B = [ord(x) - ord('a') for x in s2]
        
        target = [0] * 26
        for x in A:
            target[x] += 1
        
        window = [0] * 26
        for i, x in enumerate(B):
            window[x] += 1
            if i >= len(A):
                window[B[i - len(A)]] -= 1
            if window == target:
                return True
        return False