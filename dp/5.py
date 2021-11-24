#5. Longest Palindromic Substring
class Solution(object):
    #O(n^2), O(1)
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
        
#https://leetcode.com/problems/longest-palindromic-substring/discuss/900639/Python-Solution-%3A-with-detailed-explanation-%3A-using-DP
    def DPlongestPalindrome(self, s):
        longest_palindrom = ''
        dp = [[0]*len(s) for _ in range(len(s))]
        #filling out the diagonal by 1
        for i in range(len(s)):
            dp[i][i] = True
            longest_palindrom = s[i]
			
        # filling the dp table
        for i in range(len(s)-1,-1,-1):
				# j starts from the i location : to only work on the upper side of the diagonal 
            for j in range(i+1,len(s)):  
                if s[i] == s[j]:  #if the chars mathces
                    # if len slicied sub_string is just one letter if the characters are equal, we can say they are palindomr dp[i][j] =True 
                    #if the slicied sub_string is longer than 1, then we should check if the inner string is also palindrom (check dp[i+1][j-1] is True)
                    if j-i ==1 or dp[i+1][j-1] is True:
                        dp[i][j] = True
                        # we also need to keep track of the maximum palindrom sequence 
                        if len(longest_palindrom) < len(s[i:j+1]):
                            longest_palindrom = s[i:j+1]
                
        return longest_palindrom
        