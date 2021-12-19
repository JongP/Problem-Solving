class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk=[]
        curNum=0
        
        for c in s:
            if c=="(":
                stk.append(curNum)
                curNum=0
            else:
                if curNum==0:
                    curNum=stk.pop()+1
                else:
                    curNum=stk.pop()+curNum*2
            
        return curNum