import sys
input = sys.stdin.readline

n = int (input())
lines = []

for _ in range(n):
    lines.append(tuple(map(int,input().rstrip().split())))
lines.sort()

dp=[1]*n

for i in range(n):

    for j in range(i):
        if lines[i][1]>lines[j][1]:
            dp[i]= dp[i] if dp[i]>dp[j]+1 else dp[j]+1


print(n-max(dp))