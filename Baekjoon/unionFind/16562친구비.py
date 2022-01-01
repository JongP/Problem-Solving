import sys
input=lambda: sys.stdin.readline().rstrip()

#map(int,input().split())
sys.setrecursionlimit(10**5)

n,m,k=map(int,input().split())
p=list(map(lambda x: -1*int(x),input().split()))

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

    if p[a]<p[b]:
        p[a]=b
    else:
        p[b]=a

for _ in range(m):
    a,b=map(lambda x:int(x)-1,input().split())
    union(a,b)

sumNum=-1*sum(filter(lambda x: x<0,p))
if k>=sumNum:
    print(sumNum)
else:
    print("Oh no")

