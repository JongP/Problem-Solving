class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk=[]
        
        for n in num:
            while k>0 and stk and stk[-1]>n:
                stk.pop()
                k-=1
            stk.append(n)
        
        while k>0 and stk:
            stk.pop()
            k-=1
        
        return str(int("".join(stk))) if stk else "0"  #"10" "2"

#https://leetcode.com/problems/remove-k-digits/discuss/88668/Short-Python-one-O(n)-and-one-RegEx
def removeKdigits(self, num, k):
    out = []
    for d in num:
        while k and out and out[-1] > d:
            out.pop()
            k -= 1
        out.append(d)
    return ''.join(out[:-k or None]).lstrip('0') or '0'