import sys
input = sys.stdin.readline

dp = [0]*101
dp[1]=1
dp[2]=1
dp[3]=1
dp[4]=2
dp[5]=2
dpLen=5

t= int(input())
ansList=[]

for _ in range(t):
    n=int(input())

    if n<=dpLen:
        ansList.append(dp[n])
        continue
    
    for i in range(dpLen+1, n+1):
        dp[i]=dp[i-1]+dp[i-5]
    ansList.append(dp[n])
    dpLen=n

for i in ansList:
    print(i)