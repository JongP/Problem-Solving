class Solution:
    #O(n*log(k)) O(n)
    def numberOfArrays(self, s: str, k: int) -> int:
        modulo=10**9+7
        dp=[-1]*len(s)
        
        def helper(idx):
            if dp[idx]!=-1: return dp[idx]
            if s[idx]=="0":
                dp[idx]=0
                return 0
            
            
            num=0
            res=0
            trav=idx
            while trav<len(s):
                num=num*10+int(s[trav])
                if k<num:
                    break
                if trav+1<len(s):
                    res=(res+helper(trav+1))%modulo #first mistake
                else:
                    res+=1
                    
                trav+=1
            
            dp[idx]=res%modulo
            return res
        
        helper(0)
        
        return dp[0]%modulo



#https://leetcode.com/problems/restore-the-array/discuss/585554/C%2B%2BPython-Simple-DP-with-python
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        s = [*map(int, s)] + [math.inf] # for easier implementation
        dp = [0] * n + [1]
        for i in range(n - 1, -1, -1):
            num, j = s[i], i + 1
            while 1 <= num <= k and j < n + 1:
                dp[i] = (dp[i] + dp[j]) % 1000000007
                num = 10 * num + s[j]
                j += 1
        return dp[0]