import sys
input=lambda : sys.stdin.readline().rstrip()

n=int(input())

nodes=[list(map(int,input().split()))+[i]  for i in range(n)]

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



edges=[]


for j in range(3):
    nodes.sort(key=lambda x:x[j])
    for i in range(len(nodes)-1):
        edges.append((abs(nodes[i][j]-nodes[i+1][j]),nodes[i][-1],nodes[i+1][-1]))


edges.sort()

res=0
cnt=0
for c,a,b in edges:
    if cnt==n-1:
        break
    if union(a,b):
        res+=c
        cnt+=1

print(res)