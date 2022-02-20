class Solution:
    def isEven(self,num):
        total=0
        while num:
            num,rem=divmod(num,10)
            total+=rem
            
        return total%2==0
    
    def countEven(self, num: int) -> int:
        res=0
        
        for i in range(1,num+1):
            if self.isEven(i): res+=1
        
        return res