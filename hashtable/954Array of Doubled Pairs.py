class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        cnter=collections.Counter(arr)
        
        if cnter[0]>0:
            if cnter[0]%2==1:
                return False
            cnter[0]=0
        
        
        for key in sorted(cnter.keys()):
            if cnter[key]==0: continue
            
            if key<0:
                if key%2==1 or cnter[key//2]-cnter[key]<0:
                    return False
                
                cnter[key//2]-=cnter[key]
                cnter[key]=0
                
                
            elif key>0:
                if cnter[key*2]-cnter[key]<0:
                    return False
                cnter[key*2]-=cnter[key]
                cnter[key]=0
                
            
            
        
        return True
        
        