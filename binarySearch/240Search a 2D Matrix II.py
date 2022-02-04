#https://www.youtube.com/watch?v=FOa55B9Ikfg
#searching == how to redcue search space? 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c=len(matrix),len(matrix[0])
        x,y=0,c-1
        
        while x<r and y>=0:
            if matrix[x][y]==target: return True
            elif matrix[x][y]>target: y-=1
            else: x+=1
                
        return False