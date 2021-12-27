from collections import deque
import sys
input=sys.stdin.readline

t=int(input())
ansL=[]
dxdy=[(0,1),(0,-1),(1,0),(-1,0)]

for _ in range(t):
    n,m=map(int,input().rstrip().split())
    visited=[[0]*n for _ in range(m)]
    fires=deque()
    path=deque()
    graph=[]
    cnt=1

    for i in range(m):
        tmp=input().rstrip()
        for j in range(n):
            if tmp[j]=="*":
                fires.append((i,j))
                visited[i][j]=2
            elif tmp[j]=="@":
                path.append((i,j))
                visited[i][j]=1
        graph.append(tmp)
    
    escFlag=False

    while path:
        lp=len(path)
        lf=len(fires)
        for _ in range(lp):
            pX,pY= path.popleft()
            if visited[pX][pY]==2:
                continue

            for dx,dy in dxdy:
                nX,nY=pX+dx,pY+dy
                if nX<0 or nX>=m or nY<0 or nY>=n:
                    ansL.append(cnt)
                    escFlag=True
                    break
                if graph[nX][nY]!="#" and  visited[nX][nY]==0:
                    visited[nX][nY]=1
                    path.append((nX,nY))
            if escFlag:
                break
        if escFlag:
            break
        
        for _ in range(lf):
            fX,fY=fires.popleft()
            for dx,dy in dxdy:
                nX,nY=fX+dx,fY+dy
                if nX<0 or nX>=m or nY<0 or nY>=n:
                    continue
                if graph[nX][nY]!="#" and (visited[nX][nY]==0 or visited[nX][nY]==1):
                    visited[nX][nY]=2
                    fires.append((nX,nY))                
        cnt+=1
        #[print(line) for line in visited]
        #print("\n")

    if not escFlag:
        ansL.append("IMPOSSIBLE")


[print(ans) for ans in ansL]


#https://www.acmicpc.net/source/27864750

from collections import deque
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def bfs(q):
    while q:
        x, y = q.popleft()
        chk = -2 if visit[x][y] == -2 else visit[x][y]
        for i in range(4):
            dx = x + delta[i][0]
            dy = y + delta[i][1]
            if dx < 0 or dx >= h or dy < 0 or dy >= w:
                if chk != -2:
                    return visit[x][y] + 1
            else:
                if visit[dx][dy] == -1 and (building[dx][dy] == '.' or building[dx][dy] == '@'):
                    if chk == -2:
                        visit[dx][dy] = -2
                    else:
                        visit[dx][dy] = visit[x][y] + 1
                    q.append((dx, dy))

    return "IMPOSSIBLE"

for tc in range(int(input())):
    w, h = map(int, input().split())
    building = []
    start = []
    fire = []
    visit = [[-1] * w for _ in range(h)]
    for i in range(h):
        tmp = input()
        building.append(tmp)
        for j in range(w):
            if tmp[j] == '*':
                fire.append((i, j))
                visit[i][j] = -2
            elif tmp[j] == '@':
                start = (i, j)
                visit[i][j] = 0
    q = deque()
    q.extend(fire) #불을 먼저 넣어서 진행
    q.append(start)

    print(bfs(q))


