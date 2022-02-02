class Solution:
    #O(n) O(1)
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res=0
        
        for acc in accounts:
            tmp=sum(acc)
            if tmp>res: res=tmp
        
        return res