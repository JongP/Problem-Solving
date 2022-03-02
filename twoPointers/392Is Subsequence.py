class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0: return True
        idx=0
        
        for char in t:
            if char==s[idx]:
                idx+=1
                if idx==len(s):
                    return True
        return False