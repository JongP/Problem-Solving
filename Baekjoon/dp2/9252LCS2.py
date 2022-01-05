#don't forget LCS
import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())
#sys.setrecursionlimit(10**5)


text1=input()
text2=input()

text1="t"+text1
text2="t"+text2

m=len(text1)
n=len(text2)
dp=[[""]*(m) for _ in range(n)]

ans=""
for i in range(1,n):
    for j in range(1,m):
        if text1[j]==text2[i]:
            dp[i][j]=dp[i-1][j-1]+text1[j]
            if len(dp[i][j])>len(ans):
                ans=dp[i][j]
        else:
            dp[i][j]=dp[i-1][j] if len(dp[i-1][j])>len(dp[i][j-1]) else dp[i][j-1]
            

print(len(ans))
print(ans)