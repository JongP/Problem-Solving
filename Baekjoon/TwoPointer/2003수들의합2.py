import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())
#sys.setrecursionlimit(10**5)



n,m=map(int,input().split())
arr=list(map(int,input().split()))
s=e=0
res=0
sumN=arr[0]

while s<n:
    if e==n-1 or sumN>=m:
        if sumN==m:
            res+=1
        sumN-=arr[s]
        s+=1
    elif sumN<m:
        e+=1
        sumN+=arr[e]

print(res)