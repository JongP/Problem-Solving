#5. Longest Palindromic Substring
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        global maxLen
        maxLen=1
        candidates=[]
        l=len(s)
        
        if l==1:
            return s
        
        answer=s[0]
        
        #spend n to find candidates
        for i in range(l-2):
            if s[i]==s[i+1]:
                candidates.append((i,i+1))
            if s[i]==s[i+2]:
                candidates.append((i,i+2))
        if s[-1]==s[-2]:
            candidates.append((l-2,l-1))
            
        for a,b in candidates:
            tmp= self.expandPalindrome(s,a,b)
            if tmp:
                answer=s[tmp[0]:tmp[1]+1]
        
        return answer
            
            
        
            
            
    def expandPalindrome(self,s,le,ri):
        global maxLen
        
        while le>0 and ri<len(s)-1:
            if s[le-1]!=s[ri+1]:
                break
            le-=1
            ri+=1
            
        if maxLen<(ri-le+1):
            maxLen=ri-le+1
            return (le,ri)
        
        return None
        