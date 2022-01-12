import sys
input=lambda : sys.stdin.readline().rstrip()

m,n=map(int,input().split())

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

while (m,n)!=(0,0):
    """
    if n==0:
        print(0)
        continue
    """
    edges=sorted([list(map(int,input().split()))  for _ in range(n) ],key= lambda x:x[2])
    p=[-1]*m
    totalSum=sum([e[2] for e in edges])

    res=0
    cnt=0
    for a,b,c in edges:
        if union(a,b):
            res+=c
            cnt+=1
            if cnt==m-1:
                break
    print(totalSum-res)

    m,n=map(int,input().split())
