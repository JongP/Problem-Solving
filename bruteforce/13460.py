import sys
input = sys.stdin.readline
INF=int(1e9)
directions=[0,1,2,3]#down right up left

n,m = map(int,input().rstrip().split())

board=[]
redPoint=(0,0)
bluePoint=(0,0)

for i in range(n):
    row = input().rstrip()
    if 'R' in row:
        redPoint=(i,row.index('R'))
    if 'B' in row:
        bluePoint=(i,row.index('B'))

    board.append(list(row))
print(bluePoint,redPoint)
def printBoard():
    for row in board:
        print("".join(row))
    print("\n")

def oneMove(point,direction):
    x,y=point
    
    if direction==0:#down
        next_pos=x
        while board[next_pos+1][y]=='.':
            next_pos+=1
        if board[next_pos+1][y]=='O':
            return (0,0)#meet hole
        return (next_pos,y)
    elif direction==1:#right
        next_pos=y
        while board[x][next_pos+1]=='.':
            next_pos+=1
        if board[x][next_pos]=='O':
            return (0,0)#meet hole
        return (x,next_pos)
    elif direction==2:#up
        next_pos=x
        while board[next_pos-1][y]=='.':
            next_pos-=1
        if board[next_pos-1][y]=='O':
            return (0,0)#meet hole
        return (next_pos,y)
    elif direction==3:#left
        next_pos=y
        while board[x][next_pos-1]=='.':
            next_pos-=1
        if board[x][next_pos-1]=='O':
            return (0,0)#meet hole
        return (x,next_pos)

ans=INF

def oneTurn(redPoint,bluePoint,depth) :
    global ans
    if depth>=10: return

    for dir in directions:
        #printBoard()
        nextBluePoint=oneMove(bluePoint,dir)
        if nextBluePoint[0]==0: continue
        board[bluePoint[0]][bluePoint[1]]='.'
        board[nextBluePoint[0]][nextBluePoint[1]]='B'

        if (depth==1 and dir==3):
            printBoard()
            print(redPoint,nextRedPoint,bluePoint,nextBluePoint)

        nextRedPoint=oneMove(redPoint,dir)
        if nextRedPoint[0]==0:
            ans=min(ans,depth)
            continue
        
        board[redPoint[0]][redPoint[1]]='.'
        board[nextRedPoint[0]][nextRedPoint[1]]='R'

        if (depth==1 and dir==3):
            printBoard()
            print(redPoint,nextRedPoint,bluePoint,nextBluePoint)
        if (depth==2 and dir==0):
            printBoard()
            print(redPoint,nextRedPoint,bluePoint,nextBluePoint)

        oneTurn(nextRedPoint,nextBluePoint,depth+1)

        board[bluePoint[0]][bluePoint[1]]='B'
        board[nextBluePoint[0]][nextBluePoint[1]]='.'
        board[redPoint[0]][redPoint[1]]='R'
        board[nextRedPoint[0]][nextRedPoint[1]]='.'



oneTurn(redPoint,bluePoint,1)
if ans==INF:
    print(-1)
else:
    print(ans)