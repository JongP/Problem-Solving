class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        
        dp=[[-1]*n for _ in range(m)]   #dp[m][n]
        
        def helper(x,y):
            if x==m or y==n:
                return n-y or m-x
            elif dp[x][y]!=-1:
                return dp[x][y]
            
            if word1[x]==word2[y]:
                dp[x][y] = helper(x+1,y+1)
            else:#operations    
                #insert
                iVal=helper(x,y+1)

                #delete
                dVal=helper(x+1,y)

                #replace
                rVal=helper(x+1,y+1)

                dp[x][y]=min(iVal,dVal,rVal)+1
            
            return dp[x][y]
        
        
        
        
        return helper(0,0)


#iteraitve solution
#https://leetcode.com/problems/edit-distance/discuss/1475220/Python-3-solutions-Top-down-DP-Bottom-up-DP-O(N)-in-Space-Clean-and-Concise
class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[-1] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    dp[i][j] = j  # Need to insert `j` chars to become s2[:j]
                elif j == 0:
                    dp[i][j] = i  # Need to delete `i` chars to become ""
                elif s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[m][n]

class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp, dpPrev = [-1] * (n+1), [-1] * (n+1)
        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    dp[j] = j  # Need to insert `j` chars to become s2[:j]
                elif j == 0:
                    dp[j] = i  # Need to delete `i` chars to become ""
                elif s1[i-1] == s2[j-1]:
                    dp[j] = dpPrev[j-1]
                else:
                    dp[j] = min(dpPrev[j], dp[j-1], dpPrev[j-1]) + 1
            dp, dpPrev = dpPrev, dp
        return dpPrev[n]