import sys
input=lambda : sys.stdin.readline().rstrip()

n,m=map(int,input().split())
edges=sorted([list(map(int,input().split())) for _ in range(m)] , key = lambda x:x[2])

p=[-1]*n

def find(x):
    if p[x]<0:
        return x #I miswrote p[x]

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

res=0
cnt=0

for a,b,c in edges:
    if cnt==n-2:
        break

    if union(a-1,b-1):
        res+=c
        cnt+=1

print(res)