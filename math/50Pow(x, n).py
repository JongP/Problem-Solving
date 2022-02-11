class Solution:
    #this can be done O(log(n))!!
    def myPow(self, x: float, n: int) -> float:
        dp={}
        
        def helper(x,n):
            if n==0: return 1.0
            if n==1: return x
            if n in dp: return dp[n]

            if n<0:
                x=1/x
                n=-1*n
                
            dp[n]= helper(x,n//2)**2 * (1 if n%2==0 else x)
            
            return dp[n]
            
        return helper(x,n)


#https://leetcode.com/problems/powx-n/discuss/738830/Python-recursive-O(log-n)-solution-explained
class Solution:
    def myPow(self, x, n):
        if abs(x) < 1e-40: return 0 
        if n == 0: return 1
        if n < 0: return self.myPow(1/x, -n)
        lower = self.myPow(x, n//2)
        if n % 2 == 0: return lower*lower
        if n % 2 == 1: return lower*lower*x