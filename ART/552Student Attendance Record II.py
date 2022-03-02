#https://leetcode.com/problems/student-attendance-record-ii/discuss/1483377/Python-From-Top-down-DP-to-Bottom-up-DP-Clean-and-Concise
class Solution:
    #O(6n) TLE Top-down
    def checkRecord(self, n: int) -> int:
        MOD=10**9+7
        dp=[[[-1]*3  for _ in range(2)] for _ in range(n) ]
        
        dp[n-1][0][0]=dp[n-1][0][1]=3
        dp[n-1][0][2]=2
        dp[n-1][1][0]=dp[n-1][1][1]=2
        dp[n-1][1][2]=1
        

        def dfs(idx,absent,late):
            if dp[idx][absent][late]!=-1:
                #print(idx,absent,path)
                return dp[idx][absent][late]
            
            res=0
            
            #"P"
            res+=dfs(idx+1,absent,0)%MOD

            
            #"A"
            if absent==0:
                res+=dfs(idx+1,1,0)%MOD
            
            #"L"
            if late<=1:
                res+=dfs(idx+1,absent,late+1)%MOD

            
            
            
            dp[idx][absent][late]=res%MOD
            
            return dp[idx][absent][late]
        
        
        #print(dp)
        return dfs(0,0,0)

#bottom-up works..
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD=10**9+7
        dp=[[[-1]*3  for _ in range(2)] for _ in range(n) ]
        
        dp[n-1][0][0]=dp[n-1][0][1]=3
        dp[n-1][0][2]=2
        dp[n-1][1][0]=dp[n-1][1][1]=2
        dp[n-1][1][2]=1
        
        
        for i in range(n-2,-1,-1):
            for j in range(2):
                for k in range(3):
                    res=dp[i+1][j][0]
                    
                    if j==0:
                        res=(res+dp[i+1][1][0])%MOD
                    
                    if k<=1:
                        res=(res+dp[i+1][j][k+1])%MOD
                    
                    dp[i][j][k]=res
        
        
        
        #print(dp)
        return dp[0][0][0]


#other optimized solution
class Solution:  # 5128 ms, faster than 15.70%
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * 3, [0] * 3]  # dp[a][l]
        dpPrev = [[0] * 3, [0] * 3]  # dpPrev[a][l]
        for i in range(n, -1, -1):
            for a in range(1, -1, -1):
                for l in range(2, -1, -1):
                    if i == n:
                        dp[a][l] = 1
                    else:
                        dp[a][l] = dpPrev[a][0]
                        if a == 0: dp[a][l] += dpPrev[a + 1][0]
                        if l < 2: dp[a][l] += dpPrev[a][l + 1]
                        dp[a][l] %= MOD
            dp, dpPrev = dpPrev, dp

        return dpPrev[0][0]


#https://leetcode.com/problems/student-attendance-record-ii/discuss/101634/Python-DP-with-explanation
# dp[i]the number of all possible attendance (without 'A') records with length i :

# end with "P": dp[i-1]
# end with "PL": dp[i-2]
# end with "PLL": dp[i-3]
# end with "LLL": is not allowed
# so dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

# the number of all possible attendance (with 'A') records with length n:
# ∑dp[i] *dp[n-1-i] i = 0,1,...,n-1
class Solution(object):
    def checkRecord(self, n):
        if n == 1:
            return 3
        if n == 0:
            return 0
        nums = [1, 1, 2]
        i = 2
        while i < n:
            nums.append((nums[i] + nums[i-1] + nums[i-2])% 1000000007)
            i += 1
        result = (nums[n] + nums[n-1] + nums[n-2]) % 1000000007
        for i in range(n):
            result += nums[i+1] * nums[n-i] % 1000000007
            result %= 1000000007
        return result

#another important solution
#https://leetcode.com/problems/student-attendance-record-ii/discuss/101643/Share-my-O(n)-C%2B%2B-DP-solution-with-thinking-process-and-explanation