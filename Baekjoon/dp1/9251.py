#https://twinw.tistory.com/126
import sys
input = sys.stdin.readline

n1= "0"+input().rstrip()
n2= "0"+input().rstrip()
l1=len(n1)
l2= len(n2)

dp=[ 0 for _ in range(l1)]
dp2=[ 0 for _ in range(l1)]

for i in range(1,l2):
    for j in range(1,l1):
        if n2[i]==n1[j]:
            dp[j]= dp2[j-1]+1
        else:
            dp[j]= max([dp[j-1],dp2[j]])
    dp2=dp[:]

print(max(dp))