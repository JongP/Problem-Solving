class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        #build graph
        graph=collections.defaultdict(set)
        inDegrees={}
        
        for i,word in enumerate(words):
            for char in word:
                if char not in inDegrees:inDegrees[char]=0
                    
            #out word
            if i>0:
                prevWord=words[i-1]
                ptr=0
                l=min(len(word),len(prevWord))
                while ptr<l and word[ptr]==prevWord[ptr]: ptr+=1
                if ptr==l and len(prevWord)>len(word): return ""   #inserted
                if ptr<l and word[ptr] not in graph[prevWord[ptr]]:
                    graph[prevWord[ptr]].add(word[ptr])
                    inDegrees[word[ptr]]+=1

        
        
        #topological sorting
        totalLen=len(inDegrees)
        res=[]
        
        stk=[key for key in inDegrees if inDegrees[key]==0]
        
        while stk:
            cur=stk.pop()
            res.append(cur)
            
            for nxt in graph[cur]:
                inDegrees[nxt]-=1
                if inDegrees[nxt]==0:
                    stk.append(nxt)
        
        
        
        
        
        return "".join(res) if len(res)==totalLen else ""

#"abc" "ab"  ==> ""

#example solution
from collections import defaultdict
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        in_degree = defaultdict(set)
        out_degree = defaultdict(set)
        all_char = set([c for word in words for c in word]) #check this out 
                
        # build graph
        for i in range(1, len(words)):
            for c1, c2 in zip(words[i-1], words[i]):
                if c1 != c2: # c1 < c2
                    in_degree[c2].add(c1)
                    out_degree[c1].add(c2)
                    break
            
            else: # execuate at the end of the loop, break will skip
                # if second word is the prefix of the first word, in valid
                if len(words[i-1]) > len(words[i]):
                    return ''
                
        # intial nodes with no indegree
        res = [c for c in all_char if not in_degree[c]]
        queue = deque(res)
        
        while queue:
            c = queue.popleft()
            for nxt in out_degree[c]:
                in_degree[nxt].remove(c) # remove dependency
                
                if len(in_degree[nxt]) == 0: # no indegree
                    queue.append(nxt)
                    res.append(nxt)
                    
        if len(res) == len(all_char):
            return ''.join(res)
        else:       
            return '' # if not all chars in res, there is a circle
        
#complexity analysis
#https://leetcode.com/problems/alien-dictionary/solution/