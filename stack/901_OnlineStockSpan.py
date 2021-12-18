#subarray maxium
class StockSpanner:
    
    def __init__(self):
        self.stk=[]
        #self.day=0
        
    def next(self, price: int) -> int:
        depth=1
        while self.stk and self.stk[-1][0]<=price:
            depth+=self.stk.pop()[1]
        self.stk.append((price,depth))
            
        return depth