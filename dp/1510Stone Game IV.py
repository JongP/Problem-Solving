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

    cache_sqr = {}
    for i in range(1, 317):
        cache_sqr[i] = i ** 2


#example solution
class Solution:
    cache_sqr = {}
    for i in range(1, 317):
        cache_sqr[i] = i ** 2
    
    def winnerSquareGame(self, n: int) -> bool:
        @cache
        def can_win(remain):
            if not remain:
                return False
            sqr_m = sqrt(remain)
            isqr_m = floor(sqr_m)
            if sqr_m == isqr_m:
                return True
            
            for i in range(isqr_m, 0, -1):
                # if there is a way to make next player lose, then cur player wins
                if not can_win(remain - Solution.cache_sqr[i]):
                    return True
            return False
    
        return can_win(n)