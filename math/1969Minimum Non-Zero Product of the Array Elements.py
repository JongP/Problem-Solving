class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        if p==1: return 1
        
        MOD=10**9+7
        
        
        #11...110
        num =(1<<p) - 2
        
        dp={0:1}
        def helper(num,power,dp):
            if power in dp: 
                return dp[power]

            res = (helper(num,power//2,dp)%MOD)*(helper(num,power//2,dp)%MOD) #what I missed
            if power%2==1:
                res*=num
            
            dp[power]=res%MOD
            
            return res
            
        res=(num+1)* helper(num,2**(p-1)-1,dp) #num**(2**(p-1)-1)
        
        
        return res%MOD



#https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/discuss/1403913/Python-math-oneliner-with-proof-explained
class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 1_000_000_007

        def fastPow(base, power):  # base^power % MOD
            if power == 0: return 1
            res = fastPow(base, power // 2)
            res = (res * res) % MOD
            if power & 1:
                res = (res * base) % MOD
            return res
        
        lastNumber = 2 ** p - 1
        commonNumber = 2 ** p - 2
        times = lastNumber // 2

        return fastPow(commonNumber, times) * lastNumber % MOD



#greedy proof
#We can only focus on 2 numbers, for example "111000" and "000111". You will notice the smallest product should be "111110" * "000001".
#But why? Just notice that, whenever one of the multiplier is NOT 1, then the result will be shifted to the left, resulting a higher bit, which should not occur in the best answer.