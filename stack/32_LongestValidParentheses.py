class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res=0
        cur=0#cur is the most important variable. 
        stk=[]
        
        for c in s:
            if c=="(":
                stk.append(cur)
                cur=0
            elif c==")":
                if stk:
                    cur=stk.pop()+cur+1
                    if cur>res:
                        res=cur
                else:
                    cur=0#forget this state at first
    
        return res*2