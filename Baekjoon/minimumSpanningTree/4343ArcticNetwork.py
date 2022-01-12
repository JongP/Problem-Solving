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
    S,P=map(int,input().split())
    outposts=[ list(map(int,input().split()))  for _ in range(P)]    
    p=[-1]*P
    
    edges=[]
    for i in range(len(outposts)):
        for j in range(i+1,len(outposts)):
            edges.append( (sqrt((outposts[i][0]-outposts[j][0])**2 +(outposts[i][1]-outposts[j][1])**2 )    ,i,j))

    edges.sort()

    res=0
    cnt=S-1 #not S?

    for d,a,b in edges:
        if cnt==P-1:
            break
        if union(a,b):
            res=d
            cnt+=1
    
    ansL.append(res)


[print("%0.2f"%a) for a in ansL]