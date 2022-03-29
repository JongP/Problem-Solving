class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        memo=[[[math.inf]*2 for _ in range(2)] for _ in range(len(stoneValue))]
        
        def playRound(idx,isAlice,memo ):
            if idx>=len(stoneValue):
                return 0,0
            elif memo[idx][isAlice][0]!=math.inf:
                return memo[idx][isAlice]
            
            aPoint,bPoint=-1,-1
            
            val= -math.inf if isAlice else math.inf
            
            newVal=0
            for i in [0,1,2]:
                if idx+i>=len(stoneValue): continue
                
                newVal+=stoneValue[idx+i]
                aPts,bPts=playRound(idx+i+1,not isAlice,memo)
                
                if isAlice:
                    aPts+=newVal
                    if val<aPts-bPts:
                        val=aPts-bPts
                        aPoint,bPoint=aPts,bPts
                else:
                    bPts+=newVal
                    if val>aPts-bPts:
                        val=aPts-bPts
                        aPoint,bPoint=aPts,bPts
                        
                    
                    
            memo[idx][isAlice][:]= [aPoint,bPoint]
            return aPoint,bPoint
        
        aPoint,bPoint=playRound(0,True,memo)
        #print(aPoint,bPoint)
        if aPoint>bPoint:
            return "Alice"
        elif aPoint==bPoint:
            return "Tie"
        else:
            return "Bob"


#https://leetcode.com/problems/stone-game-iii/discuss/564342/JavaC%2B%2BPython-Dynamic-Programming
class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        n = len(stoneValue)
        suffixSum = [0 for _ in range(n+1)]
        dp = [0 for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            suffixSum[i] = suffixSum[i+1] + stoneValue[i]
        for i in range(n-1, -1, -1):
            dp[i] = stoneValue[i] + suffixSum[i+1] - dp[i+1]
            for k in range(i+1, min(n, i+3)):
                dp[i] = max(dp[i], suffixSum[i] - dp[k+1])
        if dp[0]*2 == suffixSum[0]:
            return "Tie"
        elif dp[0]*2 > suffixSum[0]:
            return "Alice"
        else:
            return "Bob"