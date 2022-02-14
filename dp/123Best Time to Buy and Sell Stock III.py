#unsolved
#should pracite dp more
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/135704/Detail-explanation-of-DP-solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=len(prices)
        dp=[[0]*l for _ in range(3)]
        
        
        for k in range(1,3):
            minVal=prices[0]
            
            for i in range(1,l):
                dp[k][i]=max(dp[k][i-1],prices[i]-minVal)
                if minVal>prices[i]-dp[k-1][i]: minVal=prices[i]-dp[k-1][i]
        #print(dp)
        
        return dp[2][l-1]

#https://www.youtube.com/watch?v=T9JcnpXSkes