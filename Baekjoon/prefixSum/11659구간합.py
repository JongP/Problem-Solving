import sys
input=sys.stdin.readline
N,M= map(int,input().rstrip().split())
arr=list(map(int,input().rstrip().split()))
ansL=[]

#input processessing
prefixSum=[0]*(N+1)
for i in range(1,N+1):
    prefixSum[i]=prefixSum[i-1]+arr[i-1]

#cal sum
for _ in range(M):
    a,b=map(int,input().rstrip().split())
    ansL.append(prefixSum[b]-prefixSum[a-1])

[print(ans) for ans in ansL]