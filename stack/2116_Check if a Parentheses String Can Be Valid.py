class Solution:
    #O(n) O(n) 35min
    """
    basic idea
    1) is there any open or free bracket to handle close bracket?
    2) is there any free bracket to handle left open bracket?
    ps) you can come up with stack easily in parantheses problems
    """
    def canBeValid(self, s: str, locked: str) -> bool:
        l=len(s)
        if l%2!=0:
            return False
        
        fStk=[]
        oStk=[]
        
        for i in range(l):
            v=s[i]
            lock=locked[i]
            
            if lock=="0":
                fStk.append(i)
                continue
            
            if v=="(":
                oStk.append(i)
            elif oStk:
                oStk.pop()
            elif fStk:
                fStk.pop()
            else:
                return False
            
        
        #below were the difficult part to implement at first time
        tmpStk=[]
        while fStk and oStk:
            if fStk[-1]>oStk[-1]:
                tmpStk.append(fStk.pop())
            elif not tmpStk:
                return False
            else:
                oStk.pop()
                tmpStk.pop()

        #came up with at last time
        while tmpStk and oStk:
            tmpStk.pop()
            oStk.pop()
        
            
        if oStk:
            return False
        else:
            return True

#we dont even need any stack
#https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/discuss/1646582/Python3-Java-C%2B%2B-Counting-Brackets-O(n)
    def canBeValid(self, s: str, l: str) -> bool:
        if len(s) % 2 == 1: return False
        tot = op = cl = 0 # tot -> Total variable brackets, op -> Open, cl -> Closed
        for i in range(len(s)):
            if l[i] == '0': tot += 1
            elif s[i] == '(': op += 1
            elif s[i] == ')': cl += 1
            if tot + op - cl < 0: return False 
        tot = op = cl = 0
        for i in range(len(s) - 1, -1, -1):
            if l[i] == '0': tot += 1
            elif s[i] == '(': op += 1
            elif s[i] == ')': cl += 1
            if tot - op + cl < 0: return False

        return True

"""
We iterate over the string s twice.
Count of variable brackets is maintained using tot
Count of fixed open brackets is maintained using op
Count of fixed closed brackets is maintained using cl
In forward iteration we are checking if we have too many fixed closed brackets ), this is achieved using: if tot + op - cl < 0: return False
In backward iteration we are checking if we have too many fixed open brackets (, this is achieved using: if tot - op + cl < 0: return False
"""