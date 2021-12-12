class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        l=len(nums)
        target,mod=divmod(sum(nums),2)
        
        if mod!=0:
            return False
        
        dp=[0]*(target+1)
        dp[0]=1
        
        #print(target)
        
        for i in range(1,l+1):
            num=nums[i-1]
            prevDP=dp.copy()
            for j in range(target+1):
                if prevDP[j]==1 and j+num<target+1:
                    #print(j,num)
                    dp[j+num]=1
                    if j+num==target:
                        return True
                    
        return False

#hint w/ topic(kanpsack)

#wrong
#at [1,2,5], dp calculated in modified 
    def canPartition(self, nums: List[int]) -> bool:
        l=len(nums)
        target,mod=divmod(sum(nums),2)
        
        if mod!=0:
            return False
        
        dp=[0]*(target+1)
        dp[0]=1
        
        
        for i in range(1,l+1):
            num=nums[i-1]
            for j in range(target+1):
                if dp[j]==1 and j+num<target+1:
                    dp[j+num]=1
                    if j+num==target:
                        return True
                    
                
        
        
        return False