#https://blog.naver.com/PostView.naver?blogId=kks227&logNo=220793134705&categoryNo=299&parentCategoryNo=0&viewDate=&currentPage=10&postListTopCurrentPage=&from=postList
import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())
#sys.setrecursionlimit(10**5)


n,l,i=map(int,input().split())

dp=[[-1]*(l+1) for _ in range(n+1)]

def binary(x,y):
    if dp[x][y]!=-1:
        return dp[x][y]
    if y==0 or x==0:
        dp[x][y]=1
        return 1
    
    dp[x][y]=binary(x-1,y)
    if y>0:
        dp[x][y]+=binary(x-1,y-1)
    return dp[x][y]

def skip(x,y,k):
    if x==0:
        return
    if y==0:
        while x>0:
            path.append("0")
            x-=1
        return

    pivot=binary(x-1,y)
    if k<=pivot:
        path.append("0")
        skip(x-1,y,k)
    else:
        path.append("1")
        skip(x-1,y-1,k-pivot)

binary(n,l)
path=[]
skip(n,l,i)

print("".join(path))#"0010" not "10"