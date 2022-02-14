class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stk=[]
        res=0
        
        for price in prices:
            while stk and stk[-1]>=price: stk.pop()
                
            if stk and price-stk[0]>res:
                res=price-stk[0]
            stk.append(price)
        return res