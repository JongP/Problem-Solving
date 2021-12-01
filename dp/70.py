class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n<=2:
            return n
        
        prevOne=2
        prevTwo=1
        ans=3
        idx=3
        while idx<=n:
            ans=prevOne+prevTwo
            #print(idx,ans,prevOne,prevTwo)
            prevTwo=prevOne
            prevOne=ans
            idx+=1
        
        return ans
    #[1,2,3,5,8,13,21]
    