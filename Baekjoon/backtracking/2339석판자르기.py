#solved... but I sold my soul..
N=int(input())
board=[list(map(int,input().split())) for _ in range(N)]
paddles=set()
#paddlesUsed=set()
for i in range(N):
    for j in range(N):
        if board[i][j]==1:
            paddles.add((i,j))


def isSuc(top,down,left,right):
    #0 good to search, 1 got to goal, 2 can't get to goal
    num1=0
    num2=0
    for i in range(top,down+1):
        for j in range(left,right+1):
            if board[i][j]==1:
                num1+=1
            if board[i][j]==2:
                num2+=1
    
    if num1==0 and num2==1:
        return 1
    elif num2>=2 and num1==0:
        return 2
    else:
        return 0

def trySlice(x,y,dir):#dir 0 vertiacal 1 horizontal
    if dir==1:
        #horizontal
        for i in range(y-1,-1,-1):
            if board[x][i]==-1 or board[x][i]==-3:
                break
            if board[x][i]==2:
                return False
        for i in range(y+1,N):
            if board[x][i]==-1 or board[x][i]==-3:
                break
            if board[x][i]==2:
                return False

        board[x][y]=-2
        
        for i in range(y-1,-1,-1):
            if board[x][i]==-1 or board[x][i]==-3:
                break
            elif board[x][i]==1:
                board[x][i]=-4
            else:
                board[x][i]=-2
        for i in range(y+1,N):
            if board[x][i]==-1 or board[x][i]==-3:
                break
            elif board[x][i]==1:
                board[x][i]=-4
            else:
                board[x][i]=-2
    else:
        #vertical
        for i in range(x-1,-1,-1):
            if board[i][y]==-2 or board[i][y]==-4:
                break
            if board[i][y]==2:
                return False
        for i in range(x+1,N):
            if board[i][y]==-2 or board[i][y]==-4:
                break            
            if board[i][y]==2:
                return False
        
        board[x][y]=-1

        for i in range(x-1,-1,-1):
            if board[i][y]==-2 or board[i][y]==-4:
                break
            elif board[i][y]==1:
                board[i][y]=-3
            else:
                board[i][y]=-1
        for i in range(x+1,N):
            if board[i][y]==-2 or board[i][y]==-4:
                break
            elif board[i][y]==1:
                board[i][y]=-3
            else:
                board[i][y]=-1
    return True
def restoreSlice(x,y,dir):
    board[x][y]=1
    if dir==1:
        #toUp
        for i in range(y-1,-1,-1):
            if board[x][i]==-1 or board[x][i]==-3:
                break
            if board[x][i]==-4:
                board[x][i]=1
            else:
                board[x][i]=0
        for i in range(y+1,N):
            if board[x][i]==-1 or board[x][i]==-3:
                break
            if board[x][i]==-4:
                board[x][i]=1
            else:
                board[x][i]=0
    else:
        #horizontal
        for i in range(x-1,-1,-1):
            if board[i][y]==-2 or board[i][y]==-4:
                break
            elif board[i][y]==-3:
                board[i][y]=1
            else:
                board[i][y]=0
        for i in range(x+1,N):
            if board[i][y]==-2 or board[i][y]==-4:
                break
            elif board[i][y]==-3:
                board[i][y]=1
            else:
                board[i][y]=0

def printBoard():
    print("\ncurrent Board")
    for line in board:
        print(line)

def sliceBoard(top,down,left,right,dir):#prev dir
    
    #printBoard()
    #print(top,down,left,right,dir)
    res=0
    
    if down<top or left>right:
        return 1
    tmp=isSuc(top,down,left,right)
    if tmp==2:
        return 0
    elif tmp==1:
        return 1

    #slice
    for pX,pY in paddles:
        if pX<top or pX>down or pY<left or pY>right:
            continue
        if  dir!=0 and trySlice(pX,pY,0):
            isZero=sliceBoard(top,down,left,pY-1,0)
            if isZero!=0:
                res+=isZero*sliceBoard(top,down,pY+1,right,0)
            restoreSlice(pX,pY,0)
        if dir!=1 and trySlice(pX,pY,1):
            isZero=sliceBoard(top,pX-1,left,right,1)
            if isZero!=0:
                res+=isZero*sliceBoard(pX+1,down,left,right,1)
            restoreSlice(pX,pY,1)
    #print(res)
    return res

tmpR=sliceBoard(0,N-1,0,N-1,-1)
if tmpR==0:
    print(-1)
else:
    print(tmpR)

#solution
#https://www.acmicpc.net/source/28750307
import sys

N = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
impurities = []
crystal = []
e = [-1] * 4

for i in range(N):
  for j in range(N):
    if grid[i][j] == 1:
      impurities.append([i, j])
    elif grid[i][j] == 2:
      crystal.append([i, j])

def nSomething(l, rSize, cSize, r, c):
  cnt = 0
  for x, y in l:
    if r <= x < r + rSize and c <= y < c + cSize:
      cnt += 1
  return cnt

def cut(rSize, cSize, r, c, x, y, d):

  # horizontal direction
  if d == 0:
    if nSomething(crystal, 1, cSize, x, c) == 0:
      p1 = [x - r, cSize, r, c]
      p2 = [rSize - (x - r) - 1, cSize, x + 1, c]
      return p1, p2
  else:
    if nSomething(crystal, rSize, 1, r, y) == 0:
      p1 = [rSize, y - c, r, c]
      p2 = [rSize, cSize - (y - c) - 1, r, y + 1]
      return p1, p2
  return e, e
def solve(rSize, cSize, r, c, d=-1):
  nCrystal = nSomething(crystal, rSize, cSize, r, c)
  nImpurity = nSomething(impurities, rSize, cSize, r, c)
  res = 0

  if nCrystal == 0:
    return 0
  elif nCrystal == 1:
    if nImpurity == 0:
      return 1
    else:
      return 0
  else:
    if nCrystal - nImpurity != 1:
      return 0
    
    for imp in impurities:
      x, y = imp
      if r <= x < rSize + r and c <= y < cSize + c:
        if d == -1:
          for i in range(2):
            p1, p2 = cut(rSize, cSize, r, c, x, y, i)
            a = 0 if p1 == e else solve(*p1, i ^ 1)
            b = 0 if p1 == e else solve(*p2, i ^ 1)
            res += a * b
        else:
          p1, p2 = cut(rSize, cSize, r, c, x, y, d)
          a = 0 if p1 == e else solve(*p1, d ^ 1)
          b = 0 if p1 == e else solve(*p2, d ^ 1)
          res += a * b
  return res

res = solve(N, N, 0, 0)
print(-1 if res == 0 else res)