class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:return None
        
        indexes=["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        
        def helper(digits,idx,path,res):
            if len(digits)==idx:
                res.append("".join(path))
                return
            
            for ch in indexes[int(digits[idx])-2]:
                path.append(ch)
                helper(digits,idx+1,path,res)
                path.pop()
        
        
        
        res=[]
        helper(digits,0,[],res)
        
        
        return res