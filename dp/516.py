class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        ans=0
        l=len(s)
        memo=[[-1]*l for _ in range(l)]
        for i in range(l):
            memo[i][i]=1
        
        def findLPS(s,le,ri):
            if le>ri:
                return 0
            
            if memo[le][ri]!=-1:
                return memo[le][ri]
            
            if s[le]==s[ri]:
                memo[le][ri]=findLPS(s,le+1,ri-1)+2
            else:
                memo[le][ri]= max(findLPS(s,le+1,ri),findLPS(s,le,ri-1))
            return memo[le][ri]
        
            
        
        
        return findLPS(s,0,l-1)
#solved with hint
#https://leetcode.com/problems/longest-palindromic-subsequence/discuss/99101/Straight-forward-Java-DP-solution
#first line in link
#top-down + memo approach