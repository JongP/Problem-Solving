class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res=[]
        
        def dfs(idx,path):
            if len(path)==4:
                if idx!=len(s):
                    return
                res.append(".".join(path))
                return
            elif idx>=len(s):
                return
            
            
            for i in range(3):
                if int(s[idx:idx+i+1])>255:
                    break
                
                path.append(s[idx:idx+i+1])
                dfs(idx+i+1,path)
                path.pop()
                
                if s[idx]=="0":
                    break
            
            
            
            
        dfs(0,[])
        
        return res