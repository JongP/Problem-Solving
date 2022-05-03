from sortedcontainers import SortedList
def solution(matrix, queries):
    blacks, whites = getSortedList(matrix)
    
    for i, j in queries:
        bVal, bx,by = blacks.pop(i)
        wVal, wx,wy = whites.pop(j)
        
        avg= (bVal+wVal)//2
        if (bVal+wVal)%2==0:
            matrix[bx][by] = avg
            matrix[wx][wy] = avg
        else:
            matrix[bx][by] = avg +(1 if bVal>wVal else 0) 
            matrix[wx][wy] = avg +( 1 if bVal<wVal else 0)
        
        blacks.add((matrix[bx][by] , bx, by))
        whites.add( (matrix[wx][wy],wx,wy)
        
    return matrix
    
def getSortedList(matrix):
    m,n = len(matrix),len(matrix[0])
    whites = SortedList()
    blacks =SortedList()
    for i in range(m):
        for j in range(n):
            if (i+j)%2: #black
                blacks.add((matrix[i][j],i,j))
            else:
                whites.add((matrix[i][j],i,j))
                
    return blacks, whites
                


