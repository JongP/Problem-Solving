class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        l=len(prices)
        prices.append(-float('inf'))
        
        idx=0
        
        while idx<l:
            while idx<l and prices[idx]>=prices[idx+1]: idx+=1
            
            cur=prices[idx]
            
            while idx<l and prices[idx]<=prices[idx+1]: idx+=1
            
            if idx<l:
                res+=prices[idx]-cur
            
            idx+=1
        
        
        return res


#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/208241/Explanation-for-the-dummy-like-me.
# public int maxProfit(int[] prices) {
#         int i = 0, buy, sell, profit = 0, N = prices.length - 1;
#         while (i < N) {
#             while (i < N && prices[i + 1] <= prices[i]) i++;
#             buy = prices[i];

#             while (i < N && prices[i + 1] > prices[i]) i++;
#             sell = prices[i];

#             profit += sell - buy;
#         }
#         return profit;
# }