class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastOcc={c:i for i,c in enumerate(s)}
        
        stk=["!"]
        visited=set()
        
        for i, c in enumerate(s):
            if c in visited: continue
            
            while stk[-1]>c and lastOcc[stk[-1]]>i:
                visited.remove(stk.pop())
            
            stk.append(c)
            visited.add(c)
        
        return "".join(stk[1:])