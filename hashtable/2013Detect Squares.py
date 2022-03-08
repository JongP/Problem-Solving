class DetectSquares:

    def __init__(self):
        self.points=collections.defaultdict(int)
        self.yTable=collections.defaultdict(set)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)]+=1
        self.yTable[point[1]].add(point[0])        

    def count(self, point: List[int]) -> int:
        x,y=point
        res=0
        
        for nx in self.yTable[y]:
            if nx==x: continue
            val=nx-x
            
            res+=self.points[(nx,y)]*self.points[(nx,y+val)]*self.points[(x,y+val)]
            res+=self.points[(nx,y)]*self.points[(nx,y-val)]*self.points[(x,y-val)]
            
            
                
                
        return res
        