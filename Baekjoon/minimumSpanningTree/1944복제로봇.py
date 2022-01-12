import sys
from collections import deque
input=lambda : sys.stdin.readline().rstrip()


N,M=map(int,input().split())
graph=[]

keys=[]
keyID={}

for i in range(N):
    line=input()
    for j in range(N):
        if line[j]=="S":
            start=(i,j)
        elif line[j]=="K":
            keys.append((i,j))
            keyID[(i,j)]=len(keys)-1
    graph.append(line)

keys.append(start)
keyID[start]=M

edges=[]

def BFS(node):
    cx,cy=keys[node]
    cnt=1
    vNum=0
    visited=[[False]*N for _ in range(N)]
    dists=[-1]*(M+1)
    dists[node]=0
    que=deque([(cx,cy)])
    visited[cx][cy]=True

    while que:
        l=len(que)

        for _ in range(l):
            cx,cy=que.popleft()

            for dx,dy in [(-1,0),(0,1),(1,0),(0,-1)]:
                nx,ny=cx+dx,cy+dy
                if nx<0 or nx>=N or ny<0 or ny>=N or graph[nx][ny]=="1" or visited[nx][ny]:
                    continue

                visited[nx][ny]=True
                que.append((nx,ny))
                if graph[nx][ny]=="K" or graph[nx][ny]=="S" :
                    dists[keyID[(nx,ny)]]=cnt
                    vNum+=1
                    if vNum==M:
                        return dists

        cnt+=1
    print(-1)
    exit()
    #return dists
vSet=set()
for i in range(M):
    vL=BFS(i)
    for j in range(M+1):
        if i==j or (i,j) in vSet or (j,i) in vSet: continue
        vSet.add((i,j))
        edges.append((vL[j],i,j))

edges.sort()

p=[-1]*(M+1)

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

res=0
cnt=0
for c,a,b in edges:
    if cnt==M:
        break

    if union(a,b):
        res+=c
        cnt+=1

print(res)



    