from collections import deque
import heapq
import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())

n=int(input())
graph=[]
for i in range(n):
    line=input()
    for j in range(n):
        if line[j]=="A":
            start=(i,j)
        elif line[j]=="B":
            end=(i,j)
    graph.append(line)

visited=[[-2]*n for _ in range(n)]
visited[start[0]][start[1]]=0
dxdy=[(-1,0),(0,1),(1,0),(0,-1)]#n,e,s,w
que=deque((start[0],start[1],-1))


while que:
    cx,cy,cd=que.popleft()


    for i in range(4):
        tx,ty=cx,cy
        while True: 
            nx,ny=tx+dxdy[i][0],ty+dxdy[i][1]
            if nx<0 or nx>=n or ny<0 or ny>=n  or graph[nx][ny]=="x" or visited[nx][ny]!=-2:
                break
            

            que.append((nx,ny,i))
            visited[nx][ny]=visited[cx][cy]+1
            if i!=cd:
                visited[nx][ny]+=1
            if (nx,ny)==end:
                print(visited[nx][ny])
                exit()
            tx,ty=nx,ny