from collections import defaultdict
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        res=math.inf
        
        xPoints= defaultdict(list)
        yPoints= defaultdict(list)
        
        for x,y in points:
            
            for yy in xPoints[x]:
                for xx in yPoints[y]:
                    if yy in xPoints[xx] and abs((x-xx)*(y-yy)) <res:
                        res= abs((x-xx)*(y-yy))
                        
                    
                    
            xPoints[x].append(y)
            yPoints[y].append(x)
            
            
        
        
        return res if res!=math.inf else 0


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:   
        seen = set()
        res = float('inf')
        
        for x1, y1 in points: # this is the dialogue approach 
            for x2, y2 in seen: # to avoid duplicates, to make sure other involves are all visited before, 
                if (x1, y2) in seen and (x2, y1) in seen:
                    area = abs(x1 - x2) * abs(y1 - y2)
                    if area and area < res:
                        res = area
            seen.add((x1, y1))
            
        return res if res < float('inf') else 0