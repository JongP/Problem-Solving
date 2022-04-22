class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        
        cnter=collections.Counter(s)
        possibles=[0]*26
        
        res=[]
        
        for i,v in enumerate(s):
            
            nextChar=None
            
            for char in cnter:
                if possibles[ord(char)-ord('a')]<=i:
                    if not nextChar or cnter[nextChar]<cnter[char]:
                        nextChar=char
                        
            
            if not nextChar: return ""
            
            res.append(nextChar)
            possibles[ord(nextChar)-ord('a')] = i+k
            cnter[nextChar]-=1
            if cnter[nextChar]==0:
                del cnter[nextChar]
                       
        return "".join(res)


#https://leetcode.com/problems/rearrange-string-k-distance-apart/discuss/83222/Straightforward-Python-Solution-98
from collections import defaultdict

class Solution(object):
    def rearrangeString(self, string, k):
        if not string:
            return ''

        count = defaultdict(int)
        for s in string:
            count[s] += 1
        # sort the letters according to the frequency
        stack = sorted(list(count.items()), key=lambda t: t[1])

        char, count = stack.pop()  # get most frequent character
        lst = [[char] for _ in range(count)]

        # take care of the letters with same highest freq
        while stack and stack[-1][1] == count:
            char, _ = stack.pop()
            for l in lst:
                l.append(char)

        # all the characters left
        res = ''.join(c*n for c, n in stack)
        # padding
        for i, r in enumerate(res):
            lst[i % (len(lst)-1)].append(r)

        for l in lst[:-1]:
            if len(l) < k:
                return ''

        return ''.join(''.join(l) for l in lst)