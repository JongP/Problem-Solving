from copy import deepcopy
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m,n=len(mat),len(mat[0])
        
        if self.getHash(mat)==0: return 0
        
        que=collections.deque([mat])
        
        visited=set()
        step=1
        
        while que:    
            for _ in range(len(que)):
                cur=que.popleft()
                
                
                for i in range(m):
                    for j in range(n):
                        newMat=self.getNewMat(cur,i,j)
                        
                        
                        key=self.getHash(newMat)
                        if key==0:
                            return step
                        if key in visited: continue
                        visited.add(key)
                        
                        #[print(line) for line in newMat];print()
                        
                        que.append(newMat)

            step+=1

        return -1
    
    def getNewMat(self,mat,x,y):
        res = deepcopy(mat)
        
        for nx, ny in [(x,y),(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if nx<0 or nx>=len(res) or ny<0 or ny>=len(res[0]): continue
            res[nx][ny]=1-res[nx][ny]
        
        
        return res
        
        
    def getHash(self,mat):
        res=0
        cnt=0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                res |= (mat[i][j] << cnt )
                cnt+=1
                
        return res

#optimized solution w/ bit vectdor state
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m,n=len(mat),len(mat[0])
        
        start=self.getHash(mat)
        
        if start==0: return 0
        
        que=collections.deque([start])
        visited=set([start])
        step=1
        
        while que:    
            for _ in range(len(que)):
                cur=que.popleft()
                
                
                for i in range(m):
                    for j in range(n):
                        nxt=self.getNewMat(cur,i,j,m,n)
                        
                        if nxt==0:
                            return step
                        
                        if nxt in visited: continue
                        visited.add(nxt)
                        
                        que.append(nxt)

            step+=1
        
        
        
        return -1
    
    def getNewMat(self,mat,x,y,m,n):
        ID=x*n+y
        for nx, ny in [(x,y),(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if nx<0 or nx>=m or ny<0 or ny>=n: continue
            nID=nx*n+ny
            
            mat^=(1<<nID)
        
        
        return mat
        
        
    def getHash(self,mat):
        res=0
        cnt=0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                res |= (mat[i][j] << cnt )
                cnt+=1
                
        return res

#https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/discuss/446342/JavaPython-3-Convert-matrix-to-int%3A-BFS-and-DFS-codes-w-explanation-comments-and-analysis.
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        start = sum(cell << (i * n + j) for i, row in enumerate(mat) for j, cell in enumerate(row))
        dq = collections.deque([(start, 0)])
        seen = {start}
        while dq:
            cur, step = dq.popleft()
            if not cur:
                return step
            for i in range(m):
                for j in range(n):
                    next = cur
                    for r, c in (i, j), (i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j):
                        if m > r >= 0 <= c < n:
                            next ^= 1 << (r * n + c)
                    if next not in seen:
                        seen.add(next)
                        dq.append((next, step + 1))
        return -1

#dfs
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        start = sum(cell << i * n + j for i, row in enumerate(mat) for j, cell in enumerate(row)) #one liner 
        stack = [(start, 0)]
        seenSteps = {start : 0}
        while stack:
            cur, step = stack.pop()
            for i in range(m):
                for j in range(n):
                    next = cur
                    for r, c in (i, j), (i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j):
                        if m > r >= 0 <= c < n:
                            next ^= 1 << r * n + c
                    if seenSteps.get(next, float('inf')) > step + 1:
                        seenSteps[next] = step + 1
                        stack.append((next, step + 1))
        return seenSteps.get(0, -1)