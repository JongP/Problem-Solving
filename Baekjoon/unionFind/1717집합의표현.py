import sys
input=lambda: sys.stdin.readline().rstrip()

#map(int,input().split())
sys.setrecursionlimit(10**5)


n,m=map(int,input().split())
ansL=[]
p=[-1]*(n+1)

def find(a):
    if p[a]<0:
        return a
    p[a]=find(p[a])
    return p[a]

def union(a,b):
    a=find(a)
    b=find(b)
    if a==b:
        return

    p[a]=b

for _ in range(m):
    op,a,b=map(int,input().split())

    if op==1:
        a=find(a)
        b=find(b)
        if a==b:
            ansL.append("YES")
        else:
            ansL.append("NO")
    else:
        union(a,b)

[print(a) for a in ansL]