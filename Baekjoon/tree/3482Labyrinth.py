from collections import deque
import sys
input=sys.stdin.readline
#map(int,input().rstrip().split())


ansL=[]

def inRange(x,y,r,c):
    return x>=0 and x<r and y>=0 and y<c

def findStartingPoint(board,r,c):#처음거 왜 틀렸는지 생각!

    for i in range(r):
        for j in range(c):
            if board[i][j]==".":
                return (i,j)

    return (-1,-1)

def getStack(board,parent,r,c,sPoint):
    visited=[[0]*c for _ in range(r)]
    que=deque([sPoint])
    stk=[]
    visited[sPoint[0]][sPoint[1]]=1

    while que:
        cX,cY=que.popleft()
        #print(cX,cY)
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny=cX+dx,cY+dy
            if nx<0 or nx>=r or ny<0 or ny>=c or board[nx][ny]=="#" or visited[nx][ny]==1:
                continue
            visited[nx][ny]=1
            parent[nx][ny][0]=cX
            parent[nx][ny][1]=cY
            #print(nx,ny)
            que.append((nx,ny))
            stk.append((nx,ny))

    return stk

for _ in range(int(input())):
    c,r=map(int,input().rstrip().split())
    res=0
    board=[input().rstrip() for _ in range(r)]
    

    dp=[[[0,0] for _ in range(c) ] for _ in range(r)]#check
    parent=[[[0,0] for _ in range(c) ] for _ in range(r)]


    sPoint=findStartingPoint(board,r,c)
    if sPoint[0]==-1:
        ansL.append(0)
        continue
    stk=getStack(board,parent,r,c,sPoint)

    while stk:
        cx,cy=stk.pop()

        
        px,py=parent[cx][cy]

        
        if dp[px][py][1]<dp[cx][cy][1]+1:
            dp[px][py][0]=dp[px][py][1]
            dp[px][py][1]=dp[cx][cy][1]+1
        elif dp[px][py][0]<dp[cx][cy][1]+1:
            dp[px][py][0]=dp[cx][cy][1]+1


    for i in range(r):
        for j in range(c):
            if not inRange(i,j,r,c):
                exit()            
            if res < dp[i][j][1]+dp[i][j][0]:
                res = dp[i][j][1]+dp[i][j][0]



    ansL.append(res)





[print("Maximum rope length is %d."%elem) for elem in ansL]