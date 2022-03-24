class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOcc={c:i for i,c in enumerate(s)}
        
        maxReach=-1
        
        res=[]
        start=0
        idx=0
        while idx<len(s):
            if maxReach==-1:
                maxReach=lastOcc[s[idx]]
                start=idx
            elif maxReach<lastOcc[s[idx]]:
                maxReach=lastOcc[s[idx]]

                
            if idx==maxReach:
                res.append(maxReach-start+1)
                maxReach=-1
            
            idx+=1
                
                
        return res