class Solution:
    #ideal solution
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        #def dp(i)
        dp=[-1]*(367)
        dp[366]=0
        
        dayset=set(days)
        
        def helper(day):
            if dp[day]!=-1: return dp[day]
            
            if day in dayset:
                dp[day]=min( costs[i]+helper(min(366,day+v))   for i,v in enumerate([1,7,30]))                    
            else:
                dp[day]=helper(day+1)
                        
            
            
            return dp[day]
            

        helper(days[0])

        return dp[days[0]]
        
#first solution        
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        #arry input process
        arry=self.inputInit(days)
        
        #def dp(i)
        dp={-1:0}
        
        def helper(day):
            if day in dp: return dp[day]
            
            
            def cal(day,term):
                return arry[min(day+term,366)]
                
            
            dp[day]=min( costs[i]+helper(cal(day,v))  for i,v in enumerate([1,7,30]) )
            
            return dp[day]
            
        #print(arry)
        helper(days[0])
        #print(dp)
        return dp[days[0]]
        
        
        
        
    def inputInit(self,days):
        res=[-1]*367
        idx=0
        
        for i in range(1,366):
            if days[idx]<i:
                idx+=1
                if idx==len(days):
                    break
            
            res[i]=days[idx]
        
        
        return res
        