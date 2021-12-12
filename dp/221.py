import copy
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        dp=[]
        for line in matrix:
            dp.append(list(map(int,line)))
        
        ans=0
        
        upDP=[[0]*n for _ in range(m)]
        for j in range(n):
            tmp=0
            for i in range(m):
                if matrix[i][j]=="0":
                    tmp=0
                else:
                    ans=1
                    tmp+=1
                upDP[i][j]=tmp
        
        leftDP=[[0]*n for _ in range(m)]
        for i in range(m):
            tmp=0
            for j in range(n):
                if matrix[i][j]=="0":
                    tmp=0
                else:
                    tmp+=1
                leftDP[i][j]=tmp
                

        for i in range(1,m):
            for j in range(1,n):
                minN=min(leftDP[i][j],upDP[i][j])
                if minN>=dp[i-1][j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=minN
                
                dp[i][j]=min(minN,dp[i-1][j-1]+1)
                if dp[i][j]>ans:
                    ans=dp[i][j]
        #print(dp)
        
        
        return ans**2
#https://leetcode.com/problems/maximal-square/discuss/600149/Python-Thinking-Process-Diagrams-DP-Approach