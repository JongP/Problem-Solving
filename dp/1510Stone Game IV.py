class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        #O(n**1.5) O(n)
        dp=[False]*(n+1)        
        for i in range(1,n+1):
            j=1
            while j**2<=i:
                if not dp[i-j**2]:
                    dp[i]=True
                    break
                j+=1
        
        return dp[n]