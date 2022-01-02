from collections import deque
import sys
input=lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**5)

r,c=map(int,input().split())

graph=[]
visited=[[-1]*c for _ in range(r)]
birds=[]
birdsSet=set()

for i in range(r):
    line=input()
    graph.append(line)
    for j in range(c):
        if line[j]=="L":
            birds.append((i,j))
            birdsSet.add((i*c+j))
            visited[i][j]=i*c+j
        elif line[j]==".":
            visited[i][j]=i*c+j

def find(x,y):
    id=x*c+y
    if visited[x][y]==-1:
        return x*c+y
    if visited[x][y]==id:
        return id

    visited[x][y]=find(visited[x][y]//c,visited[x][y]%c)
    return visited[x][y]

def union(x1,y1,x2,y2):
    id1=find(x1,y1)
    id2=find(x2,y2)

    if id1==id2:
        return
    
    #if id1 in birdsSet and not id2 in birdsSet:
        
    if id2 in birdsSet and not id1 in birdsSet:
        visited[id1//c][id1%c]=id2
    elif id1 in birdsSet and id2 in birdsSet:
        visited[id2//c][id2%c]=id1
        birdsSet.remove(id2)
    else:
        visited[id2//c][id2%c]=id1


mQue=deque()
iniVisied=[[0]*c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if graph[i][j]!="X" and iniVisied[i][j]==0:
            que=deque([(i,j)])
            iniVisied[i][j]=1
            while que:
                cx,cy=que.popleft()

                for dx,dy in ((0,1),(0,-1),(1,0),(-1,0)):
                    nx,ny=cx+dx,cy+dy
                    if nx<0 or nx>=r or ny<0 or ny>=c :
                        continue
                    if graph[nx][ny]=="X" :
                        if iniVisied[nx][ny]==0:
                            mQue.append((cx,cy))
                            iniVisied[nx][ny]=1
                        continue
                    
                    if iniVisied[nx][ny]==0:
                        iniVisied[nx][ny]=1
                        union(cx,cy,nx,ny)
                        que.append((nx,ny))
                        """for ddx,ddy in ((0,1),(0,-1),(1,0),(-1,0)):
                            nnx,nny=nx+ddx,ny+ddy
                            if nnx<0 or nnx>=r or nny<0 or nny>=c or graph[nnx][nny]=="X":
                                continue
                            if iniVisied[nnx][nny]==1 and find(nx,ny)!=find(nnx,nny):
                                union(nx,ny,nnx,nny)"""
                    elif find(cx,cy)!=find(nx,ny):
                        union(cx,cy,nx,ny)

res=0
subQue=deque()
while(len(birdsSet)!=1):

    while mQue:
        cx,cy=mQue.popleft()
        for dx,dy in ((0,1),(0,-1),(1,0),(-1,0)):
            nx,ny=cx+dx,cy+dy
            if nx<0 or nx>=r or ny<0 or ny>=c:
                continue

            if graph[nx][ny]=="X" and visited[nx][ny]==-1:
                subQue.append((nx,ny))
                union(cx,cy,nx,ny)
                for ddx,ddy in ((0,1),(0,-1),(1,0),(-1,0)):
                    nnx,nny=nx+ddx,ny+ddy
                    if nnx<0 or nnx>=r or nny<0 or nny>=c:
                        continue
                    if visited[nnx][nny]!=-1:
                        union(nx,ny,nnx,nny)
    res+=1
    mQue,subQue=subQue,mQue


print(res)