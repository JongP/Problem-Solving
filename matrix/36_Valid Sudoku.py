class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n=9
        #row check
        for row in board:
            s=set()
            for cell in row:
                if cell==".":
                    continue
                if cell in s:
                    return False
                s.add(cell)
        #col check
        for j in range(n):
            s=set()
            for i in range(n):
                if board[i][j]==".":
                    continue
                if board[i][j] in s:
                    return False
                s.add(board[i][j])
        #square check
        for I in range(3):
            for J in range(3):
                s=set()
                for i in range(3):
                    for j in range(3):
                        if board[3*I+i][3*J+j]==".":
                            continue
                        if board[3*I+i][3*J+j] in s:
                            return False
                        s.add(board[3*I+i][3*J+j])
                        
        return True


#what a nice solution
#https://leetcode.com/problems/valid-sudoku/discuss/15451/A-readable-Python-solution
def isValidSudoku(self, board):
    return (self.is_row_valid(board) and
            self.is_col_valid(board) and
            self.is_square_valid(board))

def is_row_valid(self, board):
    for row in board:
        if not self.is_unit_valid(row):
            return False
    return True

def is_col_valid(self, board):
    for col in zip(*board):#I thkn I can use this later
        if not self.is_unit_valid(col):
            return False
    return True
    
def is_square_valid(self, board):
    for i in (0, 3, 6):
        for j in (0, 3, 6):
            square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not self.is_unit_valid(square):
                return False
    return True
    
def is_unit_valid(self, unit):
    unit = [i for i in unit if i != '.']
    return len(set(unit)) == len(unit)