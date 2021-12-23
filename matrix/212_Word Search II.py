#from collections import defaultdict
class Solution:
    
    def makeTrie(self,words):
        trie={}
        
        for word in words:
            trav=trie
            
            for char in word:
                if char not in trav:
                    trav[char]={}
                trav=trav[char]
                trav["#"]=char
            
            trav["*"]=word
            
        return trie
        
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m,n=len(board),len(board[0])
        trie=self.makeTrie(words)
        res=set()
        #print(trie)
        
        
        def goDFS(board,trav,x,y):
            dxdy=[(0,1),(0,-1),(1,0),(-1,0)]
            

        
            if x<0 or x>=m or y<0 or y>=n or board[x][y] not in trav:
                return False
            
            nTrav=trav[board[x][y]]
            board[x][y]=" "
            
            if "*" in nTrav:
                res.add(nTrav["*"])
            
            for dx,dy in dxdy:
                goDFS(board,nTrav,x+dx,y+dy)
                
                
            board[x][y]=nTrav["#"]
            
            return False
            
            
        
        
        
        for i in range(m):
            for j in range(n):
                goDFS(board,trie,i,j)
        
        
        
        return list(res)
        
        
        
        

#optimal solution removing trie
#dirty code to completey remove whole.
class Solution:
    
    def makeTrie(self,words):
        trie={}
        
        for word in words:
            trav=trie
            
            for char in word:
                if char not in trav:
                    trav[char]={}
                trav=trav[char]
                trav["#"]=char
            
            trav["*"]=word
            
        return trie
        
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m,n=len(board),len(board[0])
        trie=self.makeTrie(words)
        res=set()
        #print(trie)
        
        
        def goDFS(board,trav,x,y):
            dxdy=[(0,1),(0,-1),(1,0),(-1,0)]
            

        
            if x<0 or x>=m or y<0 or y>=n or board[x][y] not in trav:
                return False
            
            nTrav=trav[board[x][y]]
            board[x][y]=" "
            
            if "*" in nTrav:
                res.add(nTrav["*"])
                del(nTrav["*"])
                if len(nTrav)==1:
                    board[x][y]=nTrav["#"]
                    return True
            
            for dx,dy in dxdy:
                if goDFS(board,nTrav,x+dx,y+dy):
                    del(nTrav[board[x+dx][y+dy]])
                    if len(nTrav)==1:
                        board[x][y]=nTrav["#"]
                        return True
                    
         
            board[x][y]=nTrav["#"]
            
            return False
            
            
        
        
        for i in range(m):
            for j in range(n):
                if goDFS(board,trie,i,j):
                    del(trie[board[i][j]])
        
        print(trie)
        
        return list(res)
        
        
        
        
        
        