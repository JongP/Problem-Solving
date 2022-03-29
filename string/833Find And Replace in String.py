class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        res=[]
        
        idx=0
        sIdx=0
        hashMap={v:i for i,v in enumerate(indices)}
        
        while idx<len(s):
            if idx in hashMap:
                sIdx=hashMap[idx]
                if sources[sIdx] == s[idx:idx+len(sources[sIdx])]:
                    res.append(targets[sIdx])
                else:
                    res.append(s[idx:idx+len(sources[sIdx])])
                    
                idx+=len(sources[sIdx])
                
            else:
                res.append(s[idx])
                idx+=1
                
        res.append(s[idx:])
        
        
        return "".join(res)