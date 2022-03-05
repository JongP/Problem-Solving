#hint on main idea     #https://leetcode.com/problems/delete-and-earn/discuss/177307/Python-solution
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        maxN,minN=-math.inf,math.inf
        cnter={}
        for num in nums:
            cnter[num]=cnter.get(num,0)+1
            if num>maxN:maxN=num
            if num<minN:minN=num
            
            
        pprev=prev=0
        
        for i in range(minN,maxN+1):
            if i not in cnter: continue
             
            if i-1 in cnter:
                cur=max(pprev+cnter[i]*i,prev)
            else:
                cur=prev+cnter[i]*i
                
            prev,pprev=cur,prev
            
            
        return cur
        