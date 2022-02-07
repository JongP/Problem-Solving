class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        couter={}
        for c in s:
            couter[c]=couter.get(c,0)+1
        
        for c in t:
            if c not in couter or couter[c]<=0: return c
            else: couter[c]-=1