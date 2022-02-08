# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        
        
        def findVertical(x,y1,y2):
            if y1==y2: return 1
            
            res=0
            mid=(y1+y2)//2
            
            if sea.hasShips(Point(x,mid),Point(x,y1)):
                res+=findVertical(x,y1,mid)
            if sea.hasShips(Point(x,y2),Point(x,mid+1)):
                res+=findVertical(x,mid+1,y2)
            
            
            
            return res
            
        
        def helper(topRight,bottomLeft):
            if topRight.x==bottomLeft.x:
                return findVertical(bottomLeft.x,bottomLeft.y,topRight.y)
            
            res=0
            mid=(topRight.x+bottomLeft.x)//2
            
            if sea.hasShips(Point(mid,topRight.y),bottomLeft):
                res+=helper(Point(mid,topRight.y),bottomLeft)
            if sea.hasShips(topRight,Point(mid+1,bottomLeft.y)):
                res+=helper(topRight,Point(mid+1,bottomLeft.y))
            
            
            return res
        
        
        return helper(topRight,bottomLeft)


#https://leetcode.com/problems/number-of-ships-in-a-rectangle/discuss/441406/Python-Quartered-Search-and-O(1)-hack-for-fun
    def countShips(self, sea, P, Q):
        res = 0
        if P.x >= Q.x and P.y >= Q.y and sea.hasShips(P, Q):
            if P.x == Q.x and P.y == Q.y: return 1
            mx, my = (P.x + Q.x) / 2, (P.y + Q.y) / 2
            res += self.countShips(sea, P, Point(mx + 1, my + 1))
            res += self.countShips(sea, Point(mx, P.y), Point(Q.x, my + 1))
            res += self.countShips(sea, Point(mx, my), Q)
            res += self.countShips(sea, Point(P.x, my), Point(mx + 1, Q.y))
        return res

#https://leetcode.com/problems/number-of-ships-in-a-rectangle/discuss/440884/Python
def countShips(self, sea, topRight, bottomLeft):
    def count((x, X), (y, Y)):
        if x > X or y > Y or not sea.hasShips(Point(X, Y), Point(x, y)):
            return 0
        if (x, y) == (X, Y):
            return 1
        xm = (x + X) / 2
        ym = (y + Y) / 2
        xRanges = (x, xm), (xm+1, X)
        yRanges = (y, ym), (ym+1, Y)
        return sum(count(xr, yr) for xr in xRanges for yr in yRanges)
    return count((bottomLeft.x, topRight.x), (bottomLeft.y, topRight.y))