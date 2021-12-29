import sys
input=sys.stdin.readline
#map(int,input().rstrip().split())
res=0
n,q=map(int,input().rstrip().split())
arr=list(map(int,input().rstrip().split()))

#process prefix
prefixXOR=[0]*(n+1)
for i in range(1,n+1):
    prefixXOR[i] = prefixXOR[i-1]^arr[i-1]

for _ in range(q):
    s,e= map(int,input().rstrip().split())
    res^=prefixXOR[e]^prefixXOR[s-1]


print(res)