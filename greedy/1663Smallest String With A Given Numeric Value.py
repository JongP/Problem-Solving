class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        A=ord('a')
        #1~26
        res=['a']*n
        idx=n-1
        k-=n
        
        while k:
            #val= min(25,k)
            #k=k-val
            if k>25:
                k-=25
                val=25
            else:
                val=k
                k=0
            
            res[idx]=chr(A+val)
                
            idx-=1
            
            
            
            
        return "".join(res)