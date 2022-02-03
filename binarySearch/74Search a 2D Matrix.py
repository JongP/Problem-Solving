class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c=len(matrix),len(matrix[0])
        
        le=0
        ri=r*c-1
        
        while le<=ri:
            mid=(le+ri)//2
            x,y=mid//c,mid%c
            
            if matrix[x][y]==target:
                return True
            elif matrix[x][y]>target:
                ri=mid-1
            else:
                le=mid+1
            
            
        return False