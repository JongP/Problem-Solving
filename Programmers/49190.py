#방의 개수
#https://programmers.co.kr/learn/courses/30/lessons/49190


#board range -100,000~100,000
BOARDLEN=200001
board={}
dxdy=[(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

def setBoard(x,y,dir):
    if (x,y) not in board:
        board[(x,y)]=set([dir])
    else:
        board[(x,y)].add(dir)
def getBoard(x,y):
    if (x,y) in board: 
        return 1
    return 0

def solution(arrows):
    answer = 0
    curX,curY=0,0
    state=0
    setBoard(0,0,-1)
    for arrow in arrows:
        nextX,nextY=curX+dxdy[arrow][0],curY+dxdy[arrow][1]
        if getBoard(nextX,nextY)==1:
            if(arrow not in board[(nextX,nextY)]):
                answer+=1
        setBoard(nextX,nextY,arrow)

        curX,curY=nextX,nextY
    
    print(answer)
    return answer  
#정사각형에 대각선 생각해야

solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0])