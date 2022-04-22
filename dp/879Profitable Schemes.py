class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        m=sum(profit)
        
        dp=[[0]*(m+1) for _ in range(n+1)]
        #dp[i][j] : number of plans can be build with i people making j profit
        dp[0][0]=1
        
        
        MOD=10**9+7
        res=0 if minProfit!=0 else 1
        dic={}
        
        for g,p in zip(group,profit):
            dic.clear()
            
            #build more plans
            for i in range(n+1-g):
                for j in range(m+1):
                    if dp[i][j]!=0:
                        dic[(i+g,j+p)]=dp[i][j]
                    
                        if j+p>=minProfit:
                            res=(res+dp[i][j])%MOD
            
            #update the dp
            for (nG,nP), num in dic.items():
                #print(nG,nP)
                dp[nG][nP]=(num+dp[nG][nP])%MOD
            
        
        
        
        
        return res
        