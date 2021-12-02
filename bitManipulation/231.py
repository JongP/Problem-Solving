class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        ans=False
        
        while n:
            if n&1:
                if  n>>1:
                    return False
                return True
            n=n>>1
        return False
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and ((n & (n-1)) == 0);