class Solution:
    def countOrders(self, n: int) -> int:
        MOD=10**9+7
        prev=cur=1
        
        for i in range(2,n+1):
            cur=prev*( (i-1)*2+1 + ((i-1)*2+1)*((i-1)*2)//2 )#dp[n]= dp[n-1]*((n-1)*2+1 + aC2)
            prev=cur

        return cur%MOD
        
#https://ko.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/modular-multiplication