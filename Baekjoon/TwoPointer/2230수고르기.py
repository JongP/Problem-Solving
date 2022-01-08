import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())
#sys.setrecursionlimit(10**5)

n,m=map(int,input().split())
arr=[int(input()) for _ in range(n)]
arr.sort()


s=e=cur=0
res=int(2e9)
while s<n-1:
    if cur>=m:
        if res>cur:
            res=cur
        s+=1
        cur=arr[e]-arr[s]
    elif e==n-1:
        break
    elif cur<m:
        e+=1
        cur=arr[e]-arr[s]

print(res)