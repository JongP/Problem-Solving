class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.indices=[]
        self.numbers=[]
        self.cur=0
        self.curLe=0
        
        for i in range(0,len(encoding),2):
            if encoding[i]==0: continue
            
            self.indices.append(encoding[i] + (self.indices[-1] if i!=0 else 0))
            self.numbers.append(encoding[i+1])

        
    def next(self, n: int) -> int:
        if self.curLe==len(self.indices): return -1
        
        self.cur+=n
        
        self.myBisect(self.indices,self.cur)
        
        return self.numbers[self.curLe] if self.curLe!=len(self.indices) else -1
        
        
    def myBisect(self,indices,cur):
        le,ri=self.curLe,len(indices)-1
        res=len(indices)
        
        while le<=ri:
            mid=(le+ri)//2
            
            if indices[mid]>=cur:
                res=mid
                ri=mid-1
            else:
                le=mid+1
                
        self.curLe=res

            
    


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)

#https://leetcode.com/problems/rle-iterator/discuss/204726/Three-solutions-you-would-want-to-discuss-in-an-interview-(O(n)-O(logn)-and-O(1)-lookup)
#various time and space trade off. lookup time complexity