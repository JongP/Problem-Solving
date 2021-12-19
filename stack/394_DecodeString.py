class Solution:

    #stk solution  17% 93%
    #first mistake w/o setting tmpD which implies that digits can more than 1-digit number
    def decodeString(self, s: str) -> str:
        s="1["+s+"]"#we dont need this actually
        stk=[]
        tmp=""
        tmpD=""
        for char in s:
            
            if char.isdigit():
                tmpD+=char

            elif char=="[":
                stk.append((int(tmpD),tmp))
                tmpD=""
                tmp=""
            elif char=="]":
                digit,chars=stk.pop()
                tmp=chars+tmp*digit
            elif char.isalpha():
                tmp+=char        
        
        
        
        return tmp



    #recursion solution/ 83%, 19%
    def decodeString(self, s: str) -> str:
        s="1["+s+"]"
        stk=[]
        tmp=""
        tmpD=""

        def helper(s,idx):
            tmp=""
            tmpD=""
            i=idx
            while i<len(s):
                if s[i].isdigit():
                    tmpD+=s[i]
                elif s[i]=="[":
                    chars,tmpI=helper(s,i+1)
                    tmp+=chars*int(tmpD)
                    tmpD=""
                    i=tmpI+1
                    continue
                elif s[i]=="]":
                    return tmp,i
                elif s[i].isalpha():
                    tmp+=s[i]   
                i+=1
            return tmp
       
        
        return helper(s,0)

#solution in discussion
#https://leetcode.com/problems/decode-string/discuss/87662/Python-solution-using-stack
    def decodeString(self, s):
        stack = []; curNum = 0; curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString