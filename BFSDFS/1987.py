import sys
ip = sys.stdin.readline

r,c =tuple(map(int,ip().rstrip().split()))

board=[]
for _ in range(r):
    board.append(ip().rstrip())


max=0

def DFS(x,y,trace,depth):
    global max
    max = max if max>depth else depth

    trace+=board[x][y]

    #print("\n%d, %d: %c loop with depth %d" %(x,y,board[x][y],depth))


    if x>0  and board[x-1][y] not in trace:
        DFS(x-1,y,trace,depth+1)
    if y<c-1 and board[x][y+1] not in trace:
        DFS(x,y+1,trace,depth+1)
    if x<r-1  and board[x+1][y] not in trace:
        DFS(x+1,y,trace,depth+1)
    if y>0  and board[x][y-1] not in trace:
        DFS(x,y-1,trace,depth+1)


DFS(0,0,"",1)



print(max)