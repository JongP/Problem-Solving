class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        dp=[0]*11
        tmpI=0
        res=0
        K=len(digits)
        nStr=str(n)
        N=len(nStr)
        mySet=set(digits)
        
        #digit input process
        for i in range(1,10):
            if i==int(digits[tmpI]):
                dp[i+1]+=1
                if tmpI<K-1:
                    tmpI+=1
            dp[i]=dp[i]+dp[i-1]
        #print(dp)
        
        
        #for N-1 digits
        tmpK=K
        for _ in range(N-1):
            res+=tmpK
            tmpK*=K
            
            
        #for N digit
        for i,v in enumerate(nStr):
            res+= dp[int(v)]*(K**(N-i-1))
            
            if v not in mySet:
                break
            if i==N-1:
                res+=1
        
            
        #print(res)
        
        return res   

#logic is same but, much simple codes
#https://leetcode.com/problems/numbers-at-most-n-given-digit-set/discuss/168279/Python-O(logN)
#think why log(n)
    def atMostNGivenDigitSet(self, D, N):
        N = str(N)
        n = len(N)
        res = sum(len(D) ** i for i in range(1, n))
        i = 0
        while i < len(N):
            res += sum(c < N[i] for c in D) * (len(D) ** (n - i - 1))
            if N[i] not in D: break
            i += 1
        return res + (i == n)