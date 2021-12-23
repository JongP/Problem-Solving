class Solution:
    #space O(n+m)
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowSet=set()
        colSet=set()
        
        for i,line in enumerate(matrix):
            for j,num in enumerate(line):
                if num==0:
                    rowSet.add(i)
                    colSet.add(j)
        
        for r in rowSet:
            for j in range(len(matrix[r])):
                matrix[r][j]=0
        
        for c in colSet:
            for line in matrix:
                line[c]=0

    #space O(1)? Nope! enumerate take space O(n)!!!!
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n=len(matrix),len(matrix[0])
        MARK=1.1
        
        def markMatrix(matrix,x,y):#do not use i,j for parameter. it mess up with i,j in for loops below
            #row update                        
            for j,num in enumerate(matrix[x]):
                if num!=0:
                    matrix[x][j]=MARK
       
            #column update
            for line in matrix:
                if line[y]!=0:
                    line[y]=MARK
                
        #mark Matrix
        for i, line in enumerate(matrix):
            for j,num in enumerate(line):
                if num==0:
                    markMatrix(matrix,i,j)
        
        
        ##updataeMatrix
        for line in matrix:
            for i,num in enumerate(line):
                if num==MARK:
                    line[i]=0
    
#O(1) w/o enumerate
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n=len(matrix),len(matrix[0])
        MARK=1.1
        
        def markMatrix(matrix,x,y):
            #row update                        
            for j in range(len(matrix[x])):
                if matrix[x][j]!=0:
                    matrix[x][j]=MARK
       
            #column update
            for line in matrix:
                if line[y]!=0:
                    line[y]=MARK
                
        #mark Matrix
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    markMatrix(matrix,i,j)
        
        
        ##updataeMatrix
        for line in matrix:
            for j in range(n) :
                if line[j]==MARK:
                    line[j]=0
                    