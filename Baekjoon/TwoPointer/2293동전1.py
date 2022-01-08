#unsolved
#hint from blog
import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())
#sys.setrecursionlimit(10**5)

n,k=map(int,input().split())
coins=[int(input()) for _ in range(n)]
dp=[[0]*n for _ in range(k+1)]
dp[0][0]=1

for i in range(0,k+1):

    for j in range(n):
        for jj in range(j,n):
            if i+coins[jj]>k:
                continue
            dp[i+coins[jj]][jj]+=dp[i][j]

#[print(line) for line in dp]
print(sum(dp[k]))