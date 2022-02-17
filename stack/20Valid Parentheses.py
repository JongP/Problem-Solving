class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        pairs={"}":"{",")":"(","]":"["}
        
        
        for c in s:
            if c in ")]}":
                if not stk or stk[-1]!=pairs[c]: return False
                stk.pop()
            else:
                stk.append(c)
                
        return not stk

#https://leetcode.com/problems/valid-parentheses/discuss/9203/Simple-Python-solution-with-stack
class Solution(object):
    def isValid(self, s):
        
        if len(s)%2!=0:
            return False
        opening = set('([{')
        matches = set([('(', ')'), ('[', ']'), ('{', '}')])
        stack = []
        
        for paren in s:
            if paren in opening:
                stack.append(paren)
            else:
                if len(stack)==0:
                    return False
                last_open = stack.pop()
                if (last_open, paren) not in  matches:
                    return False
        return len(stack)==0