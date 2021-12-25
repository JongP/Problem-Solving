class Solution:
    def calculate(self, s: str) -> int:
        stk=[(0,"+")]
        op="+"
        digit=""
        cur=0
        s+="+"
        
        esc=False
        for c in s:
            if c.isspace():
                continue
            elif c.isdigit():
                digit+=c
                continue
            elif c=="(":
                stk.append((cur,op))
                cur=0
                op="+"     
                digit=""
                continue
            

            #print(digit)
            if len(digit)==0:
                num=0
            else:
                num=int(digit)
            digit=""
            
            if op=="+":
                cur+=num
            else:
                cur-=num
        
            if c in "+-":
                op=c
            elif c==")":
                digit=str(cur)
                cur,op=stk.pop()
                continue
            
                
        return cur

#https://leetcode.com/problems/basic-calculator/discuss/62418/Python-with-stack
def calculate(self, s):
    res, num, sign, stack = 0, 0, 1, [1]
    for i in s+"+":
        if i.isdigit():
            num = 10*num + int(i)
        elif i in "+-":
            res += num * sign * stack[-1]
            sign = 1 if i=="+" else -1
            num = 0
        elif i == "(":
            stack.append(sign * stack[-1])
            sign = 1
        elif i == ")":
            res += num * sign * stack[-1]
            num = 0
            stack.pop()
    return res