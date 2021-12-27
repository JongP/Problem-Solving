from collections import deque
import sys
input=sys.stdin.readline

visited=set()
dxdy=[(1,0),(-1,0),(0,1),(0,-1)]
start=""
for _ in range(3):
    start+="".join(input().rstrip().split())


def decodeString(cur):
    graph=[list(cur[i:i+3]) for i in range(0,7,3)]
    zIdx=cur.index("0")
    x,y = divmod(zIdx,3)
    return graph,x,y%3

def encodeGraph(graph):
    tmp=""
    for line in graph:
        tmp+="".join(line)
    return tmp

#print(start)
visited.add(start)
que=deque([start])
cnt=0
while que:
    l=len(que)
    for _ in range(l):
        cur=que.popleft()
        if cur=="123456780":
            print(cnt)
            exit()

        graph,x,y=decodeString(cur)
        #print(graph,x,y)
        encodeGraph(graph)
        for dx,dy in dxdy:
            nX,nY=x+dx,y+dy
            if nX<0 or nX>=3 or nY<0 or nY>=3:
                continue
            graph[x][y]=graph[nX][nY]
            graph[nX][nY]="0"
            code=encodeGraph(graph)
            graph[nX][nY]=graph[x][y]
            graph[x][y]="0"
            if code not in visited:
                visited.add(code)
                que.append(code)
    cnt+=1




print(-1)