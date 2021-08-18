import sys
input = sys.stdin.readline

n = int(input())

dp=[0]*1000000 #num of idx+1

dp[0]=1
dp[1]=2

for i in range(2,n):
    dp[i]=(dp[i-2]+dp[i-1])%15746
print(dp[n-1])

