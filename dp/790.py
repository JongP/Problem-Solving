class Solution:
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
        dp[3]=5
        dpSum[3]=dpSum[2]+dp[3]
        
        for i in range(4,n+1):
            #don't forget to add 2. You can build totally new blocks without previous blocks
            dp[i]=(dp[i-1]+dp[i-2]+2*dpSum[i-3]+2)%modulo
            dpSum[i]=(dpSum[i-1]+dp[i])%modulo
        
        return dp[n]