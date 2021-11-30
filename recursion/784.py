class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        s=s.lower()
        ans=[]
        def goDFS(string,idx,tmp,ans):
            if idx==len(string):
                ans.append(tmp)
                return
            
            
            goDFS(string,idx+1,tmp+string[idx],ans)
            if string[idx].isalpha():
                goDFS(string,idx+1,tmp+string[idx].upper(),ans)
            
            
            
            return
        
        goDFS(s,0,"",ans)
        
        return ans