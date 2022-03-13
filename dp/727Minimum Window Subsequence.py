class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        n,m=len(s1),len(s2)
        dp=[[-2]*m for _ in range(n)]
        answer=[-math.inf,math.inf]
        
        def helper(s1,s2,idx1,idx2):
            if idx2==len(s2):
                return idx1-1
            elif idx1==len(s1):
                return -1
            
            if dp[idx1][idx2]!=-2:
                return dp[idx1][idx2]
            
            if s1[idx1]==s2[idx2]:
                dp[idx1][idx2]=helper(s1,s2,idx1+1,idx2+1)
                if idx2==0:
                    helper(s1,s2,idx1+1,idx2)
            elif s1[idx1]!=s2[idx2]:
                dp[idx1][idx2]=helper(s1,s2,idx1+1,idx2)
            
            
            if idx2==0 and s1[idx1]==s2[idx2] and dp[idx1][idx2]!=-1 and dp[idx1][idx2]-idx1<=answer[1]-answer[0]:
                answer[:]=[idx1,dp[idx1][idx2]]
                
            
                
                
            return dp[idx1][idx2]
            
        
        helper(s1,s2,0,0)
        #print(dp)
        #print(answer)
        return s1[answer[0]:answer[1]+1] if answer[0]!=-math.inf else ""


#sliding window
#https://leetcode.com/problems/minimum-window-subsequence/discuss/512645/Easy-To-Understand-%3A-Sliding-window-2-pointer-Find-then-Improve
def minWindow(self, S, T):
	
    # Find - Get ending point of subsequence starting after S[s]
    def find_subseq(s):
        t = 0
        while s < len(S):
            if S[s] == T[t]:
                t += 1
                if t == len(T):
                    break
            s += 1
        
        return s if t == len(T) else None       # Ensure last character of T was found before loop ended
    
    # Improve - Get best starting point of subsequence ending at S[s]
    def improve_subseq(s):
        t = len(T) - 1
        while t >= 0:
            if S[s] == T[t]:
                t -= 1
            s -= 1
        
		return s+1
    
    s, min_len, min_window = 0, float('inf'), ''
    
    while s < len(S):
        end = find_subseq(s)            # Find end-point of subsequence
        if not end:
            break
            
        start = improve_subseq(end)     # Improve start-point of subsequence

		if end-start+1 < min_len:       # Track min length
            min_len = end-start+1
            min_window = S[start:end+1]
        
        s = start+1                     # Start next subsequence search

    return min_window