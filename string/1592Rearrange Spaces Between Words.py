class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaceNum=sum(1 for c in text if c.isspace())
        text=text.split()
        
        if len(text)!=1:
            val,extra=divmod(spaceNum,len(text)-1)
        else:
            val,extra=0,spaceNum
        
        res=[text[0]]
        
        for i in range(1,len(text)):
            res.append(" "*val) 
            res.append(text[i])
            
        res.append(" "*extra)
            
            
        return "".join(res)