#poorly solved
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        lD=len(str(low))
        hD=len(str(high))
        res=[]
        
        def generateInit(x):
            res=0
            digit=1
            while x:
                res=res*10+digit
                digit+=1
                x-=1
            return res
        
        def generate(x,res):
            trav=generateInit(x)
            initD=1
            while True:
                
                if low<=trav<=high:
                    res.append(trav)
                elif trav>high: #important
                    break
                
                if initD+x==10:
                    break
                    
                    
                trav= (trav%(10**(x-1)))*10+initD+x
                initD+=1
        
        
        for i in range(lD,hD+1):
            generate(i,res)
            
        return res

#https://leetcode.com/problems/sequential-digits/discuss/853592/Python-Solution-using-queue-explained
    def sequentialDigits(self, low, high):
        out = []
        queue = deque(range(1,10))
        while queue:
            elem = queue.popleft()
            if low <= elem <= high:
                out.append(elem)
            last = elem % 10
            if last < 9: queue.append(elem*10 + last + 1)
                    
        return out