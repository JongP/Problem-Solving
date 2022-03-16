class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.hashmap=collections.defaultdict(int)
        self.times=times
        self.winner=[]
        cur=-1
        votes=0
        for p,t in zip(persons,times):
            self.hashmap[p]+=1
            
            if self.hashmap[p]>=votes:
                cur=p
                votes=self.hashmap[p]
                
            self.winner.append(cur)

    def q(self, t: int) -> int:
        idx=self.myBisect(self.times,t)
        return self.winner[idx] 
                
    
    def myBisect(self,arry,t):
        le,ri=0,len(arry)-1
        res=-1
        
        while le<=ri:
            mid=(le+ri)//2
            
            if arry[mid]<=t:
                res=mid
                le=mid+1
            else:
                ri=mid-1
            
        
        return res
        
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)