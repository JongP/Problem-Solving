import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())
#sys.setrecursionlimit(10**5)

n,m,k=map(int,input().split())

dp=[[-1]*(m+1) for _ in range(n+1) ]

for j in range(m+1):
    dp[1][j]=1


def generate(x,y,prev):
    if dp[x][y]!=-1:
        return dp[x][y]

    res=0
    i=prev
    while i*x<=y:
        res+=generate(x-1,y-i,i)

        i+=1

    dp[x][y]=res
    return res


generate(n,m,1)

def degenerate(x,y,k,prev,path):
    if x==1:
        path.append(str(y))
        return

    pivot=0
    i=prev
    while i*x<=y:
        tmp=pivot
        pivot+=dp[x-1][y-i]
        if pivot>=k:
            path.append(str(i))
            degenerate(x-1,y-i,k-tmp,i,path)
            return
        i+=1


res=[]
degenerate(n,m,k,1,res)
print(" ".join(res))

