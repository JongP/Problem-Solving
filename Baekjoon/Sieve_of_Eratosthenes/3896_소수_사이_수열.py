import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())
#sys.setrecursionlimit(10**5)

maxN=1299709

p=[i for i in range(maxN+1)]
dp=[True]*(maxN+1)
dp[1]=False
prev=0
for i in range(2,maxN+1):
    if not dp[i]:
      p[i]=prev
      p[prev]+=1 
      continue
    p[i]=1
    prev=i
    for j in range(i*i,maxN+1,i) :
        dp[j]=False

#print(p[:20])
for _ in range(int(input())):   
    num=int(input())
    if dp[num]:
        print(0)
        continue
    print(p[p[num]])