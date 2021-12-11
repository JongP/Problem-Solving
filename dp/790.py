class Solution:
    #O(n), O(n)   --> space complexity can be optimized with 3 variables.
    def numTilings(self, n: int) -> int:
        if n<=2:
            return [1,2][n-1]
        
        modulo=10**9+7
        dp=[0]*(n+1)
        dpSum=[0]*(n+1)
        
        
        dp[1]=1
        dpSum[1]=1
        
        dp[2]=2
        dpSum[2]=dpSum[1]+dp[2]

        
        for i in range(3,n+1):
            #don't forget to add 2. You can build totally new blocks without previous blocks
            dp[i]=(dp[i-1]+dp[i-2]+2*dpSum[i-3]+2)%modulo
            dpSum[i]=(dpSum[i-1]+dp[i])%modulo
        
        return dp[n]

    def numTilings(self, n: int) -> int:
        f0,f1,f2 = 0,1,1
        for i in range(n-1):
            f0,f1,f2 = f1,f2,2*f2+f0
        return f2 % 1_000_000_007