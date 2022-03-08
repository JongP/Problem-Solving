from collections import deque
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        dp={1:[deque(["0"]),deque(["1"]),deque(["8"])],0:[deque([""])]}
        
        ADDS=[("1","1"),("6","9"),("8","8"),("9","6"),("0","0")]
        res=[]
        
        def backtrack(idx,path):
            if idx==n:
                res.append("".join(path))
                return
                
            for a,b in ADDS:
                if idx==n-2 and a=="0": continue
                path.appendleft(a)
                path.append(b)
                backtrack(idx+2,path)
                path.popleft()
                path.pop()
                
            
        for p in dp[n%2]:    
            backtrack(n%2,p)
        
        return res 