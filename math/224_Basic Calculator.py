class Solution:
    def calculate(self, s: str) -> int:
        stk=[(0,"+")]
        op="+"
        digit=""
        cur=0
        s+="+"
        
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
#we only need the sign effect on final result,
#better than below one
#https://leetcode.com/problems/basic-calculator/discuss/62418/Python-with-stack
def calculate(self, s):
    res, num, sign, stack = 0, 0, 1, [1]
    for i in s+"+":
        if i.isdigit():
            num = 10*num + int(i)#we have num in int
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

#https://leetcode.com/problems/basic-calculator/discuss/62344/Easy-18-lines-C%2B%2B-16-lines-Python
def calculate(self, s):
    total = 0
    i, signs = 0, [1, 1]
    while i < len(s):#we don't need to use for loop cuz of the consecutive digits.
        c = s[i]
        if c.isdigit():
            start = i
            while i < len(s) and s[i].isdigit():
                i += 1
            total += signs.pop() * int(s[start:i])
            continue
        if c in '+-(':
            signs += signs[-1] * (1, -1)[c == '-'], #nice code
        elif c == ')':
            signs.pop()
        i += 1
    return total


"""
  remaining   sign stack      total
3-(2+(9-4))   [1, 1]            0
 -(2+(9-4))   [1]               3
  (2+(9-4))   [1, -1]           3
   2+(9-4))   [1, -1, -1]       3
    +(9-4))   [1, -1]           1
     (9-4))   [1, -1, -1]       1
      9-4))   [1, -1, -1, -1]   1
       -4))   [1, -1, -1]      -8
        4))   [1, -1, -1, 1]   -8
         ))   [1, -1, -1]      -4
          )   [1, -1]          -4
              [1]              -4
"""