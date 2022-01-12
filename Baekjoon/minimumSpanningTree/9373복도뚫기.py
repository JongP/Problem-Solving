#unsolved
#https://blog.naver.com/PostView.naver?blogId=kks227&logNo=220799105543&categoryNo=299&parentCategoryNo=0&viewDate=&currentPage=2&postListTopCurrentPage=1&from=postList&userTopListOpen=true&userTopListCount=30&userTopListManageOpen=false&userTopListCurrentPage=2
#https://bedamino.tistory.com/11
#let's check from the shortest one --> kruskal
import sys
from math import sqrt
input=lambda : sys.stdin.readline().rstrip()


ansL=[]

def find(x):
    if p[x]<0:
        return x
    p[x]=find(p[x])
    return p[x]

def union(x,y):
    x=find(x)
    y=find(y)
    if x==y:
        return False
    p[x]+=p[y]
    p[y]=x
    return True


for _ in range(int(input())):
    w=int(input())
    n=int(input())
    sensors=[list(map(int,input().split()))  for _ in range(n)]
    p=[-1]*(n+2)
    edges=[(w,n,n+1)]
    for i in range(n):
        for j in range(i+1,n):
            edges.append((sqrt((sensors[i][0]-sensors[j][0])**2 + (sensors[i][1]-sensors[j][1])**2)-sensors[i][2]-sensors[j][2],i,j))
        edges.append(( (sensors[i][0]-sensors[i][2])  ,i,n))
        edges.append(( (w-sensors[i][0]-sensors[i][2])  ,i,n+1))
    
    edges.sort(key=lambda x:x[0])

    for c,a,b in edges:
        if union(a,b) and find(n)==find(n+1):
            ansL.append(c/2)
            break




[print(round(a,6) if a>0 else 0) for a in ansL]