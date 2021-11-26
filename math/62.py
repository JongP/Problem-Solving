class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a=m-1
        b=n-1
        
        if a==0 or b==0:
            return 1
        
        #a>b
        
        if a<b:
            tmp=a
            a=b
            b=tmp
            
        ans=1
        
        for i in range(a+1,a+b+1):
            ans*=i
            
        for j in range(1,b+1):
            ans/=j
        return int(ans)

#https://leetcode.com/problems/unique-paths/discuss/254228/Python-3-solutions%3A-Bottom-up-DP-Math-Picture-Explained-Clean-and-Concise
    def simpleUniquePaths(self, m: int, n: int) -> int:
        ans = 1
        j = 1
        for i in range(m, m+n-2 + 1):
            ans *= i
            ans //= j
            j += 1
            
        return ans