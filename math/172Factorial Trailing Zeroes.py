class Solution:
    def trailingZeroes(self, n: int) -> int:
        res=0
        prime=5
        
        while prime<=n:
            res+=n//prime
            prime=prime*5
        
                
        return res