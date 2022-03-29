#https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
#3. Longest Substring Without Repeating Characters
from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        def isNoRepeat(dicts):
            for key in dicts:
                if dicts[key] >1:
                    return False
            return True
        
        if len(s)==0:
            return 0
        
        le=0
        ri=0
        windSize=1
        dicts=defaultdict(int)
        dicts[s[0]]+=1
        
        while ri<len(s)-1:
            if not isNoRepeat(dicts):
                dicts[s[le]]-=1
                le+=1
                ri+=1
                dicts[s[ri]]+=1
                continue
            
            while ri<len(s)-1 and dicts[s[ri+1]]==0:
                dicts[s[ri+1]]=1
                ri+=1
            if ri<len(s)-1:
                dicts[s[le]]-=1
                le+=1
                ri+=1
                dicts[s[ri]]+=1
                
    
        return ri-le+1
#https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1731/A-Python-solution-85ms-O(n)
    def bestSolution(self,s):
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)
                
            used[c] = i

        
        return max_length