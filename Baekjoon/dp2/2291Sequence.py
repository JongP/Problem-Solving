import sys

input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())
#sys.setrecursionlimit(10**5)

n,m,k=map(int,input().split())

dp=[[[-1]*(221) for _ in range(m+1)] for _ in range(n+1)]

def solver(x,y,z):
    if dp[x][y][z]!=-1:
        return dp[x][y][z]
    if x==1:
        if y>=z:
            return 1
        else:
            return 0

    res=0
    for i in range(z,int(y/x)+1):#fast think
        res+=solver(x-1,y-i,i)
    
    dp[x][y][z]=res
    return res

def tracker(k,x,y,z,res):
    if x==1:
        res.append(y)
        return
    prev=total=0
    for i in range(z,int(y/x)+1):
        total+= solver(x-1,y-i,i)
        if prev<k<=total:
            res.append(i)
            tracker(k-prev,x-1,y-i,i,res)
            break
        prev=total


    return

    
res=[]
solver(n,m,1)
tracker(k,n,m,1,res)
print(*res)