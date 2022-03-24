#hint on topic(two pointer)
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
            
        people.sort(reverse=True)    
        res=0
        le,ri=0,len(people)-1
        
        while le<=ri:
            if people[le]+people[ri]<=limit:
                le+=1
                ri-=1
            else:
                le+=1
            res+=1
        return res
            
        
        
        