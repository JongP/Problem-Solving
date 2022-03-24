#leet code hint 3
class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        m,n=len(grid),len(grid[0])
        if m==1 or n==1: return True
        
        for i in range(1,m):
            state=grid[0][0]==grid[i][0]
            for j in range(1,n):
                if (grid[i][j]==grid[0][j])!=state:
                    return False
                
        return True