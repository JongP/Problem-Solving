from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount==0:
            return 0
        
        dp=[int(2e9)]*(amount+1)
        que=deque()
        
    
            
        dp[0]=0
        que.append(0)
        
        while que:
            #print(dp)
            cur = que.popleft()
            
            for coin in coins:
                if cur+coin>amount:
                     continue
                elif cur+coin==amount:
                    return dp[cur]+1
                
                if dp[cur+coin]>dp[cur]+1:
                    dp[cur+coin]=dp[cur]+1
                    que.append(cur+coin)
                
                    
        return -1