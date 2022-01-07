import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())
#sys.setrecursionlimit(10**5)


maxN=1000001
dp=[True]*maxN
arr=[]

def isNum(x):
    s=set([x])

    while x!=1:
        tmp=x
        xx=0
        while tmp:
            m,r=divmod(tmp,10)
            xx+=r**2
            tmp=m
        x=xx
        if x in s:
            return False
        s.add(x)

    return True

for i in range(2,maxN):
    if not dp[i]:
        continue
    arr.append(i)
    for j in range(i*i,maxN,i):
        dp[j]=False


n=int(input())

idx=2
while idx<len(arr) and arr[idx]<=n:
    if isNum(arr[idx]):
        print(arr[idx])
    idx+=1
