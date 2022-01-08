import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())
#sys.setrecursionlimit(10**5)

n,m=map(int,input().split())
arr=list(map(int,input().split()))

s=e=0
sumN=arr[0]
res=int(2e9)
while s<n:
    if sumN>=m:
        if res>e-s+1:
            res=e-s+1
        sumN-=arr[s]
        s+=1
    elif e==n-1:
        break
    else:
        e+=1
        sumN+=arr[e]

if res==int(2e9):
    print(0)
else:
    print(res)
