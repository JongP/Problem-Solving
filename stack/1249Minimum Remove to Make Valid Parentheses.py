class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        inValid=set()
        stk=[]
        
        for i,c in enumerate(s):
            if c=="(": 
                stk.append(i)
            elif c==")":
                if not stk:
                    inValid.add(i)
                else:
                    stk.pop()
            
            
        for i in stk:
            inValid.add(i)
        
        
        res=[]
        
        for i,c in enumerate(s):
            if i not in inValid:
                res.append(c)
                
        return "".join(res)
        
        
            