class Solution:
    def countArrangement(self, n: int) -> int:
        
        dp={(1<<n)-1:1}
        
        
        def backtracking(used,depth,n):
            if used in dp:
                return dp[used]
            
            if depth>n:
                return 0
            
            dp[used]=sum(backtracking(used|(1<<(i-1)),depth+1,n) for i in range(1,n+1) if (depth%i==0 or i%depth==0) and used&(1<<(i-1))==0 )
        
            return dp[used]
        return backtracking(0,1,n)
        