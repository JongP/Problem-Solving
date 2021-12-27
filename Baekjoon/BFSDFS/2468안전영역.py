import sys
input=sys.stdin.readline


sys.setrecursionlimit(10**5)

n=int(input())
graph=[]
maxL,minL=-1,int(2e9)
for _ in range(n):
    tmp=list(map(int,input().rstrip().split()))
    maxL=max(maxL,max(tmp))
    minL=min(minL,min(tmp))
    graph.append(tmp)

#print(maxL,minL)
#print(graph)
dxdy=[(0,1),(0,-1),(1,0),(-1,0)]
res=1




visited=[[0]*n for _ in range(n)]
for level in range(minL,maxL):
    for ti in range(n):
        for tj in range(n):
            visited[ti][tj]=0
    cnt=0
    stk=[]

    for i in range(n):
        for j in range(n):
            if graph[i][j]>level and visited[i][j]==0:
                stk.append((i,j))
                while stk:
                    x,y=stk.pop()
                    visited[x][y]=1
                    for dx,dy in dxdy:
                        nx,ny=x+dx,y+dy
                        if nx<0 or ny<0 or nx>=n or ny>=n or graph[nx][ny]<=level:
                            continue
                        if visited[nx][ny]==0:
                            stk.append((nx,ny))



                cnt+=1


    if res<cnt:
        res=cnt

print(res)