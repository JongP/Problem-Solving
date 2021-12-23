class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n=len(matrix),len(matrix[0])
        states=[(0,1),(1,0),(0,-1),(-1,0)]
        bounds=[n,m-1]
        res=[]
        state=0
        curX,curY=0,-1
        
        while True:
            if bounds[state%2]==0:
                break
                
            for _ in range(bounds[state%2]):
                curX,curY=curX+states[state][0],curY+states[state][1]
                res.append(matrix[curX][curY])
            
            bounds[state%2]-=1
            state=(state+1)%4
            
        
        return res




#https://leetcode.com/problems/spiral-matrix/discuss/20579/Simple-Python-solution-by-mutating-the-matrix
def spiralOrder(self, matrix):
    ret = []
    while matrix:
        ret += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                ret.append(row.pop())
        if matrix:
            ret += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                ret.append(row.pop(0))
    return ret
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        matrix = deque(deque(row) for row in matrix); ret = []
        while True:
            ret += matrix.popleft()
            if not matrix: break
                
            ret += (row.pop() for row in matrix)
            if not matrix[0]: break
            
            ret += reversed(matrix.pop())
            if not matrix: break

            ret += (row.popleft() for row in reversed(matrix))
            if not matrix[0]: break
        
        return ret