from collections import deque

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #creating trie
        trie={}
        
        for word in wordDict:
            cur=trie
            for c in word:
                if c not in cur:
                    cur[c]={}
                cur=cur[c]
            cur["*"]=True
        #print(trie)
        
        travs=deque([trie])
        #trav=trie
        
        for c in s:
            flag=True
            l=len(travs)
            
            if l==0:
                return False
            
            for _ in range(l):
                trav=travs.popleft()
                if flag and "*" in trav and c in trie:
                    travs.append(trie[c])
                    flag=False

                if c in trav:
                    travs.append(trav[c])

                
        for trav in travs:
            if "*" in trav:
                return True
        return False
        