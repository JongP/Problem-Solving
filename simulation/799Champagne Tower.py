#hint on iteration
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        #if query_row==0: return poured
        
        que=[poured]
        
        for _ in range(query_row):
            newQ=[0]
            
            for i,v in enumerate(que):
                if v<1: v=1
                newQ[i]+=(v-1)/2
                newQ.append((v-1)/2)
                
            que=newQ

        return min(que[query_glass],1)

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        @lru_cache(None)
        def dp(r, c): # dp(r, c) means the amount of champagne is poured into cup[r, c]
            if c < 0 or c > r: return 0 # Invalid position
            if r == 0 and c == 0: return poured # Amount Champaign is poured into the top cup
            return max(dp(r - 1, c - 1) - 1, 0) / 2 + max(dp(r - 1, c) - 1, 0) / 2

        ans = dp(query_row, query_glass)
        return min(ans, 1)