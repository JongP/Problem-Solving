class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board),len(board[0])
        visited=[[0]*n for _ in range(m)]
        
        def helper(board,word,visited,x,y,idx):
            dxdy=[(0,1),(0,-1),(1,0),(-1,0)]
            
            if idx==len(word)-1 and board[x][y]==word[-1]:
                return True
            
            
            for dx,dy in dxdy:
                nX,nY= x+dx,y+dy
                if nX>=0 and nX<m and nY>=0 and nY<n and board[nX][nY]==word[idx+1] and visited[nX][nY]==0:
                    visited[nX][nY]=1
                    if helper(board,word,visited,nX,nY,idx+1):
                        return True
                    visited[nX][nY]=0
                    
            
            
            return False
            
            
        
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    visited[i][j]=1
                    if helper(board,word,visited,i,j,0):
                        return True
                    visited[i][j]=0
                    
                    
        return False

#how to optimize space in DFS without using vistied
#cdo everything inside DFS unlike mine
#https://leetcode.com/problems/word-search/discuss/27660/Python-dfs-solution-with-comments.

    def exist(self, board, word):
        if not board:
            return False
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    # check whether can find word, start at (i,j) position    
    def dfs(self, board, i, j, word):
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian 
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
        or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])#look at this!
        board[i][j] = tmp
        return res