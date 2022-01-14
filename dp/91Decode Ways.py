class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp=[-1]*len(s)
        
        def helper(idx):
            if idx>=len(s):
                return 1
            
            if dp[idx]!=-1:
                return dp[idx]
            
            res=0
            #decode one character
            firstDigit=int(s[idx])
            if 1<=firstDigit<=9:
                res+=helper(idx+1)            
            
            #decode two characters
            if idx<len(s)-1:
                secondDigit=int(s[idx+1])
                code=firstDigit*10+secondDigit
                if 10<=code<=26:
                    res+=helper(idx+2)
            dp[idx]=res
            return res
        
        return helper(0)


#exmaple solution
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = { len(s) : 1 }
        
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            
            res = dfs(i+1)
            if (i+1<len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"))):
                res += dfs(i+2)
            dp[i] = res
            return res
        
        return dfs(0)
