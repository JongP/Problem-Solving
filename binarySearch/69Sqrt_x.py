class Solution:
    def mySqrt(self, x: int) -> int:
        le,ri=0,x
        res=x
        
        while le<=ri:
            mid=(le+ri)//2
            
            if mid*mid<=x:
                res=mid
                le=mid+1
            else:
                ri=mid-1
                
        return res