class Solution:
    def calculate(self, s: str) -> int:
        cache=[0,"+"]
        tmpCache=[1,"*"]
        digit=""
        cur=None

        def updateTmp(tmpCache,digit):
            if tmpCache[1]=="*":
                return tmpCache[0]*int(digit)
            else:
                return tmpCache[0]//int(digit)


        for c in s:
            if c.isspace():
                continue
            elif c.isdigit():
                digit+=c
                continue

            cur=updateTmp(tmpCache,digit)
            digit=""
            
                
            if c=="+" or c=="-":
                if cache[1]=="+":
                    cache[0]+=cur
                else:
                    cache[0]-=cur
                cache[1]=c
                tmpCache=[1,"*"]
            elif c=="*" or c=="/":
                tmpCache[0]=cur
                tmpCache[1]=c

        
        cur=updateTmp(tmpCache,digit)
        
                    
        if cache[1]=="+":
            return cache[0]+cur
        else:
            return cache[0]-cur

    

class Solution2:
    def calculate(self, s: str) -> int:
        cache=[0,"+"]
        tmpCache=[1,"*"]
        digit=""
        cur=None

        def updateTmp(tmpCache,digit):
            if tmpCache[1]=="*":
                return tmpCache[0]*int(digit)
            else:
                return tmpCache[0]//int(digit)

        def updateCache(cache,cur):
            if cache[1]=="+":
                cache[0]+=cur
            else:
                cache[0]-=cur            

        for c in s:
            if c.isspace():
                continue
            elif c.isdigit():
                digit+=c
                continue

            cur=updateTmp(tmpCache,digit)
            digit=""
                
            if c=="+" or c=="-":
                updateCache(cache,cur)
                cache[1]=c
                tmpCache=[1,"*"]
                
            elif c=="*" or c=="/":
                tmpCache[0]=cur
                tmpCache[1]=c

        
        cur=updateTmp(tmpCache,digit)
        updateCache(cache,cur)
                    
        return cache[0]

#simple solution
#https://leetcode.com/problems/basic-calculator-ii/discuss/63076/Python-short-solution-with-stack.
    def calculate(self, s):
        num, stack, sign = 0, [], "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                num = 0
                sign = s[i]
        return sum(stack)