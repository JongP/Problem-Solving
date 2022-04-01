class Solution:
    def expand(self, s: str) -> List[str]:
        res=[]
        def dfs(idx,path):
            if idx==len(s):
                res.append("".join(path))
                return
            
            if s[idx].isalpha():
                path.append(s[idx])
                dfs(idx+1,path)
                path.pop()
                return
            
            candidates=[]
            
            for i in range(idx+1,len(s),2):
                candidates.append(s[i])
                if s[i+1]=="}":
                    break
                    
            candidates.sort()
            
            for c in candidates:
                path.append(c)
                dfs(i+2,path)
                path.pop()
        
        
        dfs(0,[])
            
        return res