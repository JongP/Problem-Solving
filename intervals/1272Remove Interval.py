class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res=[]
        A,B=toBeRemoved
        
        for a,b  in intervals:
            if b<=A or B<=a:
                res.append([a,b])
            else:
                if a<A:
                    res.append([a,A])
                if B<b:
                    res.append([B,b])

        return res