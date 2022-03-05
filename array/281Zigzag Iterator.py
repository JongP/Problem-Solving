class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.res=[]
        
        idx=0
        
        while idx<len(v1) or idx<len(v2):
            if idx<len(v1):
                self.res.append(v1[idx])
            if idx<len(v2):
                self.res.append(v2[idx])
            idx+=1
            
        self.iter=0

    def next(self) -> int:
        ret=self.res[self.iter]
        self.iter+=1
        return ret
        

    def hasNext(self) -> bool:
        return self.iter<len(self.res)
        