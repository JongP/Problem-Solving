from collections import defaultdict, deque
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie=self.makeTrie(words)
        res=0
        que=defaultdict(deque)
        
        for n in trie:
            que[n].append(trie[n])    
        
        
        for c in s:
            q=que[c]
            
            for _ in range(len(q)):
                cur=q.popleft()
                for key in cur:
                    if key=="*":
                        res+=cur[key]
                    else:
                        que[key].append(cur[key])
                
                
                
        
        return res
        
        
        
        
    def makeTrie(self,words):
        res={}
        for word in words:
            trav=res
            for c in word:
                if c not in trav: trav[c]={}
                trav=trav[c]
            trav["*"]=trav.get("*",0)+1
        return res
                 