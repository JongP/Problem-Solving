import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())
#sys.setrecursionlimit(10**5)

maxN=123456*2

prefixSum=[0]*(maxN+1)
dp=[True]*(maxN+1)
dp[1]=False

for i in range(2,maxN+1):
    prefixSum[i]=prefixSum[i-1]
    if not dp[i]:
        continue
    prefixSum[i]+=1

    for j in range(i*i,maxN+1,i):
        dp[j]=False


num=int(input())
while num:
    print(prefixSum[num*2]-prefixSum[num])

    num=int(input())