#-------------- Pigeonhole principle---------------#

#my inefficient solution
#but somehow I finished it in 45 mins w/o any hint
#but seems hint would have been helpful
class Solution:
    #1 + 10 + 100 + 1000 + 10000
    def smallestRepunitDivByK(self, k: int) -> int:
        if k==1:
            return k
        elif k%2==0 or k%5==0:
            return -1
        
        
        modL=[1%k]
        prefixSum=[1%k]
        modS=set([1%k])
        
        
        while True:
            newMod=modL[-1]*10%k
            if newMod in modS:
                break
            modL.append(newMod)
            modS.add(newMod)
            prefixSum.append(prefixSum[-1]+modL[-1])
            
            if prefixSum[-1]%k==0:
                return len(modL)

        
        #print(modL,prefixSum)
        
        i=0
        newSet=set([el%k for el in prefixSum])
        while True:
            prefixSum.append(prefixSum[-1]+modL[i%len(modL)])
            if prefixSum[-1]%k==0:
                return len(modL)+i+1            
            
            if prefixSum[-1]%k in newSet:
                break
            newSet.add(prefixSum[-1]%k)
            
            i+=1
        
        
        return -1
        
        
#example solution with hint "11111 = 1111 * 10 + 1 We only need to store remainders modulo K."
#https://leetcode.com/problems/smallest-integer-divisible-by-k/discuss/260875/Python-O(K)-with-Detailed-Explanations
class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 10 not in {1, 3, 7, 9}: return -1
        mod, mod_set = 0, set()
        for length in range(1, K + 1):
            mod = (10 * mod + 1) % K
            if mod == 0: return length
            if mod in mod_set: return -1
            mod_set.add(mod)
        return -1

#solution with deep understanding on 