class Solution:
    def myAtoi(self, s: str) -> int:
        state=0
        idx=0
        sign=1
        res=0
        
        while idx<len(s) and s[idx]==" ": idx+=1
        
        if idx<len(s) :
            if s[idx]=="-":
                sign=-1
                idx+=1
            elif s[idx]=="+":
                idx+=1
        
            
            
        while idx<len(s) and s[idx].isdigit():
            
            res=10*res+ord(s[idx])-ord('0')
            if (sign==1 and res>(1<<31)-1):
                return (1<<31)-1
            elif(sign==-1 and res>(1<<31)) :
                return -1*(1<<31)
            
            idx+=1
            
            
        
            
        
        
        return res*sign