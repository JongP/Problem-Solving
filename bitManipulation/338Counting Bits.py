class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[0]
        power=1
        nPower=2
        
        for i in range(1,n+1):
            if i==nPower:
                power<<=1
                nPower<<=1
            
            res.append(res[i-power]+1)
            
            
        return res