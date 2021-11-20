#https://gsmesie692.tistory.com/113
import sys
input = sys.stdin.readline

n,k = tuple(map(int,input().rstrip().split()))
dp = [ [0]*(k+1) for _ in range(n+1)]

stuffs = []
for _ in range(n):
    stuffs.append(tuple(map(int,input().rstrip().split())))

max=0
for i in range(1,n+1):
    w ,v = stuffs[i-1]
    for j in range(1,k+1):
        if w>j:
            dp[i][j]=dp[i-1][j]
            continue

        new_value = dp[i-1][j-w]+v
        if new_value>dp[i-1][j]:
            dp[i][j]=new_value
        else:
            dp[i][j]=dp[i-1][j]
        if dp[i][j]>max:
            max=dp[i][j]
print(max)

