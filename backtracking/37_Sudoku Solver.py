class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n=9
        
        def validateUnit(lst):
            s=set()
            for elem in lst:
                if elem==".":
                    continue
                if elem in s:
                    return False
                s.add(elem)
            return True

        def validateRow(x):
            return validateUnit(board[x]) 
        
        def validateCol(y):
            return validateUnit([line[y]   for line in board])
        
        def validateSub(x,y):
            X,Y=(x//3)*3,(y//3)*3
            return validateUnit([board[X+i][Y+j] for i in range(3) for j in range(3)])
        
                
            
        def backtracking(x,y):
            
            #validity
            if not validateRow(x) or not validateCol(y) or not validateSub(x,y):
                return False
                                
            #goal
            if x==8 and y==8:
                return True
                                
            
            #traversing
            flag=False
            while x<n:
                while y<n:
                    #print(x,y,board[x][y])
                    if board[x][y]==".":
                        flag=True
                        break
                    y+=1
                if flag:
                    break
                y=0
                x+=1
            if x==9:x,y=8,8
            
            if x==8 and y==8 and board[x][y]!=".":
                return True
                                
            
            #choice
            for num in range(1,10):
                #print(x,y)
                board[x][y]=str(num)
                if backtracking(x,y):
                    return True
                board[x][y]="."
            
            return False   #don't forget
                                
            
        backtracking(0,0)


#example fast solution
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Init the helper variables
        row_used = [set() for _ in range(9)]
        col_used = [set() for _ in range(9)]
        sub_boxes_used = [[set() for _ in range(3)] for _ in range(3)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                row_used[i].add(int(board[i][j]))
                col_used[j].add(int(board[i][j]))
                sub_boxes_used[i // 3][j // 3].add(int(board[i][j]))
        
        self._solve(board, row_used, col_used, sub_boxes_used, 0)
        
        return board
    
    def _solve(self, board, row_used, col_used, sub_boxes_used, index):
        if index >= 81:
            return True
        
        i, j = index % 9, index // 9 #iterating in matrix
        
        if board[i][j] != '.':
            return self._solve(board, row_used, col_used, sub_boxes_used, index + 1)
        
        for attempt in range(1, 10):
            if (attempt in row_used[i]) \
                or (attempt in col_used[j]) \
                or (attempt in sub_boxes_used[i // 3][j // 3]):
                continue
            
            row_used[i].add(attempt)
            col_used[j].add(attempt)
            sub_boxes_used[i // 3][j // 3].add(attempt)
            board[i][j] = str(attempt)
            
            if self._solve(board, row_used, col_used, sub_boxes_used, index + 1):
                return True
            
            board[i][j] = '.'
            row_used[i].remove(attempt)
            col_used[j].remove(attempt)
            sub_boxes_used[i // 3][j // 3].remove(attempt)
        
        return False