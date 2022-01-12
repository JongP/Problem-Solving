import sys
import math
input=lambda : sys.stdin.readline().rstrip()

n=int(input())

p=[-1]*n

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


def getDist(x,y):
    return math.sqrt((points[x][0]-points[y][0])**2 + (points[x][1]-points[y][1])**2)


points=[list(map(float,input().split()))  for _ in range(n)]
edges=[]
for i in range(len(points)):
    for j in range(i+1,len(points)):
        edges.append((getDist(i,j),i,j))

edges.sort()

res=0
cnt=0
for d,a,b in edges:
    if cnt==n-1:
        break

    if union(a,b):
        res+=d
        cnt+=1

print(res)