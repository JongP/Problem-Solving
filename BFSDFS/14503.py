import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
r,c,d= map(int,input().rstrip().split())

graph =[list(map(int,input().rstrip().split())) for _ in range(n)]


dxdy=[(0,-1),(-1,0),(0,1),(1,0)]#for making turn
rear=[(1,0),(0,-1),(-1,0),(0,1)]#for going back
nextDir=[3,0,1,2]

answer=1
graph[r][c]=2

def printGraph():
    for row in graph:
        print(row)
    print("\n")

while True:
    haveToClean=0
    for _ in range(4):
        dx,dy=dxdy[d]
        if graph[r+dx][c+dy]==0:
            d=nextDir[d]
            r,c = r+dx, c+dy
            graph[r][c]=2
            answer+=1
            haveToClean=1
            break
        d=nextDir[d]


    if haveToClean==1:
        continue

    #cant clean
    dxBack,dyBack = rear[d]
    if graph[r+dxBack][c+dyBack] == 1:#wall!!
        break
    r,c= r+dxBack,c+dyBack



print(answer)