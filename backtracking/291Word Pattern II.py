#Shouldn't it be n^m instead? I think the recurrence relation would sum up to sum((jCi * j) for i in [0, m] for j in [i, n]).
# This is bounded by n^m   n=len(s), m=len(pattern)
# T(m, n) = T(m - 1, n - 1) + T(m - 1, n - 2) + ...
class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        pD={}
        sD={}
        
        def helper(pattern,s,pIdx,sIdx,pD,sD):
            if pIdx==len(pattern) or sIdx==len(s):
                if pIdx==len(pattern) and sIdx==len(s): return True
                else: return False

            if pattern[pIdx] not in pD:
                for i in range(1,len(s)-sIdx+1):
                    sVal=s[sIdx:sIdx+i]
                    if sVal in sD: continue
                    
                    pD[pattern[pIdx]]=sVal
                    sD[sVal]=pattern[pIdx]
                    if helper(pattern,s,pIdx+1,sIdx+i,pD,sD): return True
                    del pD[pattern[pIdx]]
                    del sD[sVal]
                    
            
            else:
                val=pD[pattern[pIdx]]
                if len(s)-sIdx<len(val) or val!=s[sIdx:sIdx+len(val)]: return False
                if helper(pattern,s,pIdx+1,sIdx+len(val),pD,sD): return True
                
            return False
        
        
        return helper(pattern,s,0,0,pD,sD)

#https://leetcode.com/problems/word-pattern-ii/discuss/385224/Standard-Python-backtrack-solution
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def backtrack(pattern, s, i, j, ptable, wtable):
            if i == len(pattern) and j == len(s): # two pointers i, j both reach the end, means fully matched
                return True
            if i == len(pattern) or j == len(s): # only one pointer i or j reaches the end, means not matched
                return False
            p = pattern[i]
            if p in ptable:
                w = ptable[p]
                if s[j:j+len(w)] != w:
                    return False
                else:
                    return backtrack(pattern, s, i + 1, j + len(w), ptable, wtable)
            else:
                for k in range(j, len(s)):
                    word = s[j:k+1]
                    if word in wtable:
                        continue
                    ptable[p] = word
                    wtable[word] = p
                    if backtrack(pattern, s, i + 1, k + 1, ptable, wtable):
                        return True
                    ptable.pop(p)
                    wtable.pop(word)
                return False
        
        if len(s) < len(pattern):
            return False
        return backtrack(pattern, s, 0, 0, {}, {})
"""
Time complexity: let n = len(pattern) and m = len(s) (m >= n),
the problem is more like slicing the string into n nonempty pieces.
How many slicing ways? C^{n-1}{m-1}. For each slice, it takes O(n) to validate.
So the total complexity is O(n * C^{n-1}{m-1}).
"""




#https://leetcode.com/problems/word-pattern-ii/discuss/73669/Python-backtracking-48ms
    def wordPatternMatch(self, pattern, str):
        return self.dfs(pattern, str, {})

    def dfs(self, pattern, str, dict):
        if len(pattern) == 0 and len(str) > 0:
            return False
        if len(pattern) == len(str) == 0:
            return True
        for end in range(1, len(str)-len(pattern)+2): # +2 because it is the "end of an end"
    #When we find the match for pattern[0], we have len(pattern) - 1 letters left to match, therefore the maximum length of pattern[0] can only be len(str) - (len(pattern) - 1) = len(str) - len(pattern) + 1. For slicing in Python, that would make the upper-bound len(str) - len(pattern) + 2.
            if pattern[0] not in dict and str[:end] not in dict.values():
                dict[pattern[0]] = str[:end]
                if self.dfs(pattern[1:], str[end:], dict):
                    return True
                del dict[pattern[0]]
            elif pattern[0] in dict and dict[pattern[0]] == str[:end]:
                if self.dfs(pattern[1:], str[end:], dict):
                    return True
        return False

