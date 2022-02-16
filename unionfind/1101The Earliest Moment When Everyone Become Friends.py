class Solution:
    
    def find(self,x):
        if self.parents[x]<0: return x
        self.parents[x]=self.find(self.parents[x])
        return self.parents[x]
    
    def union(self,x,y):
        x=self.find(x)
        y=self.find(y)
        
        if x==y: return
        
        self.total-=1
        self.parents[x]=y
    
    
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        self.parents=[-1]*n
        self.total=n
        
        logs.sort(key=lambda x:x[0])
        
        for t,a,b in logs:
            self.union(a,b)
            if self.total==1: return t
        
        return -1