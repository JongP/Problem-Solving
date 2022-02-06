#hint to set how to make dp from leetcode
#you don;t have to fill out the dp table from 0 to len(dp)-1!!!!!!!
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs=sorted([i for i in zip(startTime,endTime,profit)])
        dp=[el[2] for el in jobs]
        
        #print(jobs)
        
        def getMax(jobs,dp,job,idx):
            res=0
            le=idx+1
            ri=len(dp)-1
            
            while le<ri:
                mid=(le+ri)//2
                
                if jobs[mid][0]>=job[1]:
                    ri=mid
                else:
                    le=mid+1
            
            
            return dp[le] if le<len(dp) and jobs[le][0]>=job[1] else 0 
        
        for i in range(len(jobs)-1,-1,-1):
            dp[i]+=getMax(jobs,dp,jobs[i],i)
            if i!=len(jobs)-1 and  dp[i]<dp[i+1]:
                dp[i]=dp[i+1]
    
        #print(dp)
        
        
        return dp[0]

#https://leetcode.com/problems/maximum-profit-in-job-scheduling/discuss/1430330/Python-dp-%2B-binary-search-explained
import bisect

class Solution:
    def jobScheduling(self, S, E, profit):
        jobs = sorted(list(zip(S, E, profit)))
        S = [i[0] for i in jobs]
        n = len(jobs)
        dp = [0] * (n + 1)
        for k in range(n-1,-1,-1):
            temp = bisect_left(S, jobs[k][1])
            dp[k] = max(jobs[k][2] + dp[temp], dp[k+1])
        return dp[0]

#https://leetcode.com/problems/maximum-profit-in-job-scheduling/solution/