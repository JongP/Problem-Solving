class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        #O(mn)
        m,n=len(matrix),len(matrix[0])
        res=0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    val=min(matrix[i-1][j] if i>0 else 0,matrix[i][j-1] if j>0 else 0,matrix[i-1][j-1] if i>0 and j>0 else 0 )
                    matrix[i][j]=val+1
                    res+=matrix[i][j]
                    
        
        
        return res
        
        