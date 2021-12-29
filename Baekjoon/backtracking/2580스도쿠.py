def solveSudoku(board):
    """
    Do not return anything, modify board in-place instead.
    """
    n=9
    
    rowSet=[set() for _ in range(n)]
    colSet=[set() for _ in range(n)]
    subSet=[[set() for _ in range(3)] for _ in range(3)] 

    for i in range(n):
        for j in range(n):
            if board[i][j]!=0:
                rowSet[i].add(board[i][j])
                colSet[j].add(board[i][j])
                subSet[i//3][j//3].add(board[i][j])   
        
    def backtracking(x,y):
        #goal
        if x==8 and y==8:
            return True
                            
        #traversing
        flag=False
        while x<n:
            while y<n:
                if board[x][y]==0:
                    flag=True
                    break
                y+=1
            if flag:
                break
            y=0
            x+=1
        if x==9:x,y=8,8
        
        if x==8 and y==8 and board[x][y]!=0:
            return True
                            
        
        #choice
        for num in range(1,10):
            #print(x,y)
            if num in rowSet[x] \
                or num in colSet[y] \
                    or num in subSet[x//3][y//3]:
                continue
            board[x][y]=num
            rowSet[x].add(num);colSet[y].add(num);subSet[x//3][y//3].add(num)
            if backtracking(x,y):
                return True
            board[x][y]=0
            rowSet[x].remove(num);colSet[y].remove(num);subSet[x//3][y//3].remove(num)
        
        return False   #don't forget
                            
        
    backtracking(0,0)
    
    
board=[list(map(int,input().split())) for _ in range(9)]
solveSudoku(board)
[print(" ".join(map(str,line))) for line in board]