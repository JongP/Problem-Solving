#Got TLE from O(n^2) solution at first
#then fixed it with a little amount of hint
from collections import defaultdict,deque

class Solution:
    def findStartEnd(self,beginWord,endWord,wordList):
        bFound=eFound=False
        b=-1
        e=-1
        i=0
        
        while i<len(wordList) and not (bFound and eFound) :
            word=wordList[i]
            
            bFlag=eFlag=True
            for j,c in enumerate(word):
                if bFlag and c!=beginWord[j]: bFlag=False
                if eFlag and c!=endWord[j]: eFlag=False
                if not bFlag and not eFlag: break
            
            if bFlag: 
                b=i
                bFound=True
            if eFlag: 
                e=i
                eFound=True
                
            i+=1
        
        if b==-1:
            wordList.append(beginWord)
            b=len(wordList)-1
            
        return b,e
            
    
    
    def initGraph(self,beginWord,wordList):
        graph=defaultdict(set)
        
 
            

        for word in wordList:
            
            for i in range(len(word)):
                key=word[:i]+"*"+word[i+1:]
                graph[key].add(word)
                graph[word].add(key)
    
       
        
        return graph
                
                
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        begin,end=self.findStartEnd(beginWord,endWord,wordList)
        wordLen=len(beginWord)
        if end==-1: return 0
        graph=self.initGraph(beginWord,wordList)
        
        res=1
        visited=set([beginWord])
        que=deque([beginWord])
        #print(begin,end)
        #print(graph)
        
        while que:
            res+=1
            for _ in range(len(que)):
                cur=que.popleft()
                #print(cur,res)
                for i in range(wordLen):
                    key=cur[:i]+"*"+cur[i+1:]
                    if key in visited: continue
                    visited.add(key)
                    for nxt in graph[key]:
                        if nxt==endWord: return res
                        if nxt in visited: continue
                        visited.add(nxt)
                        que.append(nxt)

                
        return 0
        
        



#https://leetcode.com/problems/word-ladder/discuss/40723/Simple-to-understand-Python-solution-using-list-preprocessing-and-BFS-beats-95
from collections import deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        
        def construct_dict(word_list):
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i+1:]
                    d[s] = d.get(s, []) + [word]
            return d
            
        def bfs_words(begin, end, dict_words):
            queue, visited = deque([(begin, 1)]), set()
            while queue:
                word, steps = queue.popleft()
                if word not in visited:
                    visited.add(word)
                    if word == end:
                        return steps
                    for i in range(len(word)):
                        s = word[:i] + "_" + word[i+1:]
                        neigh_words = dict_words.get(s, [])
                        for neigh in neigh_words:
                            if neigh not in visited:
                                queue.append((neigh, steps + 1))
            return 0
        
        d = construct_dict(wordList | set([beginWord, endWord]))
        return bfs_words(beginWord, endWord, d)