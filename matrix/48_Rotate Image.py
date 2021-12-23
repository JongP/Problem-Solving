class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        trav=n
        while trav>1:
            
            cX=(n-trav)//2
            
            for i in range(trav-1):
                cY=cX+i
                num=matrix[cX][cY]
                for _ in range(4):
                    cX,cY=cY,n-cX-1
                    matrix[cX][cY],num=num,matrix[cX][cY]
            
            trav-=2



#https://leetcode.com/problems/rotate-image/discuss/145237/Python-beats-100
#he got quater area in a different way with me.
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        half = (math.ceil(len(matrix) / 2))
        
        r = None
        if len(matrix) % 2 == 0:
            r = range(half)
        else:
            r = range(half - 1)

        for y in r:
            for x in range(half):
                tmp = matrix[y][x]
                matrix[y][x] = matrix[-1 - x][y]
                matrix[-1 - x][y] = matrix[-1 - y][-1 - x]
                matrix[-1 - y][-1 - x] = matrix[x][-1 - y]
                matrix[x][-1 -y] = tmp


#https://leetcode.com/problems/rotate-image/discuss/18872/A-common-method-to-rotate-the-image
"""
rotation matrix is
cos -sin
sin cos

90 degrees roation is then theta is pi/2  . watch out for the sign!! 0,0 is in lefr upper side in matrix
0 1   
-1 0

we can split this matrix into to matrix
0 1   and  -1 0
1 0        0 1
which means flip the sign of row and swap row and col.


 * clockwise rotate
 * first reverse up to down, then swap the symmetry 
 * 1 2 3     7 8 9     7 4 1
 * 4 5 6  => 4 5 6  => 8 5 2
 * 7 8 9     1 2 3     9 6 3
"""

void rotate(vector<vector<int> > &matrix) {
    reverse(matrix.begin(), matrix.end());
    for (int i = 0; i < matrix.size(); ++i) {
        for (int j = i + 1; j < matrix[i].size(); ++j)
            swap(matrix[i][j], matrix[j][i]);
    }
}

"""
 * anticlockwise rotate
 * first reverse left to right, then swap the symmetry
 * 1 2 3     3 2 1     3 6 9
 * 4 5 6  => 6 5 4  => 2 5 8
 * 7 8 9     9 8 7     1 4 7
"""
void anti_rotate(vector<vector<int> > &matrix) {
    for (auto vi : matrix) reverse(vi.begin(), vi.end());
    for (int i = 0; i < matrix.size(); ++i) {
        for (int j = i + 1; j < matrix[i].size(); ++j)
            swap(matrix[i][j], matrix[j][i]);
    }
}