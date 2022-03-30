from math import atan
from heapq import heappop,heappush

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        self.res=0
        self.dup=0
        
        
        tilts=self.getTilts(location,points)
  
        angle=(angle/180)*math.pi
        
        cnt=0
        heap=[]
        for deg in sorted(tilts.keys()):
            #heap clearance
            #print(deg)
            while heap and (deg-heap[0])>angle :
                cnt-=tilts[heappop(heap)]
            
            #heap insert
            heappush(heap,deg)
            cnt+=tilts[deg]
            
            #check answer
            if self.res<cnt:
                self.res=cnt
            
        
        
        #print(self.dup)
        
        return self.res+self.dup
        
        
    def getTilts(self,location,points): 
        tilts=collections.Counter()
        
        
        lx,ly=location
        
        for a,b in points:
            dx,dy=a-lx,b-ly
            
            if dx==0:
                if dy==0:
                    self.dup+=1
                    continue
                else:
                    deg=math.pi/2 *(dy)/abs(dy)
            else:
                deg=math.atan(dy/dx)
                
                if deg>=0 and dx<0:
                    deg-=math.pi
                elif deg <0 and dy>0:
                    deg+=math.pi
                
                
                
            tilts[deg]+=1
            tilts[deg+2*math.pi]+=1
                
        return tilts