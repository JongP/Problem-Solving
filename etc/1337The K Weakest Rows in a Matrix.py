class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        #get number of soldiers
        sols=[]
        for i in range(len(mat)):
            sols.append(self.findSols(mat[i])+1)
            
        #count sorting
        buckets=[[] for _ in range(101)]
        
        for i,num in enumerate(sols):
            buckets[num].append(i)
            
        
        #find k weak row
        res=[]
        for i in range(101):
            res.extend(buckets[i][:min(len(buckets[i]),k)])
            k-= len(buckets[i])
            
            
            if k<=0:
                break
                
        return res
        
        
        
        
        
    def findSols(self,array):
        le,ri=0,len(array)-1
        res=-1
        
        while le<=ri:
            mid=(le+ri)//2
            
            if array[mid]:
                res=mid
                le=mid+1
            else:
                ri=mid-1
        
        
        return res