import math
def getMaxSum(matrix,a,b):

    def solve(matrix,x,y):
        m,n=len(matrix),len(matrix[0])
        res=-math.inf

        def isBounded(i,j):
            return 0<=i<m and 0<=j<n

        def calArea(matrix,x,y,i,j):
            total=0
            #right up
            for _ in range(x-1):
                if not isBounded(i,j): return -math.inf
                total+=matrix[i][j]
                i,j = i-1,j+1
            #right down
            for _ in range(y-1):
                if not isBounded(i,j): return -math.inf
                total+=matrix[i][j]
                i,j = i+1,j+1

            if x==1 or y==1:
                return total+matrix[i][j]

            #left down
            for _ in range(x-1):
                if not isBounded(i,j): return -math.inf
                total+=matrix[i][j]
                i,j = i+1,j-1

            #left up
            for _ in range(y-1):
                if not isBounded(i,j): return -math.inf
                total+=matrix[i][j]
                i,j = i-1,j-1

            if x!=1 and y!=1:
                total +=calArea(matrix,x-1,y-1,i,j+1)
            return total





        for i in range(m):
            for j in range(n):
                res=max(res,calArea(matrix,x,y,i,j))
        
        return res



    return max(solve(matrix,a,b),solve(matrix,b,a))



matrix=[ 
    [1,2,3,4,0],
    [5,6,7,8,1],
    [3,2,4,1,4],
    [4,3,5,1,6]
]

print(getMaxSum(matrix,2,3))