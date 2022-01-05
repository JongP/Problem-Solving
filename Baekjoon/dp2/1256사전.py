import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())
#sys.setrecursionlimit(10**5)

n,m,k=map(int,input().split())

dp=[[0]*(m+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0]=1
for j in range(m+1):
    dp[0][j]=1

def generate(x,y):
    if dp[x][y]!=0:
        return dp[x][y]

    res=0
    #place "a"
    res+=generate(x-1,y)
    #palce "b"
    res+=generate(x,y-1)
    dp[x][y]=res
    return res

generate(n,m)

if k>dp[n][m]:
    print(-1)
    exit()

def degenerate(path,x,y,k):
    if x==0 or y==0:
        while x:
            path.append("a")
            x-=1
        while y:
            path.append("z")
            y-=1
        return

    pivot=dp[x-1][y]
    if pivot>=k:
        path.append("a")
        degenerate(path,x-1,y,k)
    else:
        path.append("z")
        degenerate(path,x,y-1,k-pivot)

res=[]
degenerate(res,n,m,k)
print("".join(res))