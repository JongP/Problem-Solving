from collections import deque
import sys
input=lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**5)

#union find
def find(num):
    x,y=num//n,num%n
    if visited[x][y]==-1:
        return visited[x][y]
    if visited[x][y]==x*n+y:
        return visited[x][y]
    visited[x][y]=find(visited[x][y])
    return visited[x][y]

def union(x1,y1,x2,y2):
    global leftK
    l1=find(x1*n+y1)
    l2=find(x2*n+y2)
    if l1==l2:
        return
    visited[l1//n][l1%n]=l2
    leftK-=1

def check(cx,cy):
    for dx,dy in ((0,1),(0,-1),(1,0),(-1,0)):
            nx,ny=cx+dx,cy+dy
            if nx<0 or nx>=n or ny<0 or ny>=n or visited[nx][ny]==-1:
                continue
            
            if find(cx*n+cy)!=find(nx*n+ny):
                union(cx,cy,nx,ny)
                if leftK==0:
                    print(cnt)
                    exit()  
            
#input process
n,k=map(int,input().split())
leftK=k-1
que=deque()
visited=[[-1]*n for _ in range(n)]

for _ in range(k):
    a,b=map(lambda x:int(x)-1,input().split())
    visited[a][b]=a*n+b
    que.append((a,b))

cnt=0
for cx,cy in que:
    check(cx,cy)    

#bfs    
cnt+=1
while que:
    l=len(que)
    for _ in range(l):
        cx,cy=que.popleft()
        
        for dx,dy in ((0,1),(0,-1),(1,0),(-1,0)):
            nx,ny=cx+dx,cy+dy
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if visited[nx][ny]==-1 :
                visited[nx][ny]=find(cx*n+cy)
                que.append((nx,ny))
            elif find(cx*n+cy)!=find(nx*n+ny):
                union(cx,cy,nx,ny)
                if leftK==0:
                    print(cnt)
                    exit()
    #[print(line) for line in visited]
    #print(leftK)
    cnt+=1



print(cnt)

#https://www.acmicpc.net/source/35023194