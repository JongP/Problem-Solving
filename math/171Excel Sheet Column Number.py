class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res=0
        
        for c in columnTitle:
            res*=26
            res+= ord(c)-ord('A')+1
        
        
        return res