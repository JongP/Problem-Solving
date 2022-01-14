class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res=0
        minEnd=points[0][1]
        
        for x1,x2 in points:
            if x1>minEnd:
                res+=1
                minEnd=x2
            elif minEnd>x2:
                minEnd=x2
                
        return res+1


#https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/discuss/887690/Python-O(n-log-n)-solution-explained
class Solution:
    def findMinArrowShots(self, points):
        points.sort(key = lambda x: x[1])
        n, count = len(points), 1
        if n == 0: return 0
        curr = points[0]
        
        for i in range(n):
            if curr[1] < points[i][0]:
                count += 1
                curr = points[i]
                
        return count  