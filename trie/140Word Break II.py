class Solution:
    def buildTrie(self,wordDict):
        trie={}
        
        for word in wordDict:
            trav=trie
            
            for c in word:
                if c not in trav: trav[c]={}
                trav=trav[c]
                    
            trav["*"] = word
            
        return trie
    
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie=self.buildTrie(wordDict)
        
        res=[]
        
        
        def dfs(idx,path):
            if idx==len(s):
                res.append(" ".join(path))
                return
            
            trav=trie
            while idx<len(s):
                if s[idx] not in trav:
                    break
                trav=trav[s[idx]]
                
                if "*" in trav:
                    path.append(trav["*"])
                    dfs(idx+1,path)
                    path.pop()
                
                idx+=1
        
        dfs(0,[])
        
        return res


#example solution
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        class Trie:
            def __init__(self, *words):
                self.root = dict()
                for word in words:
                    self.add(word)

            def add(self, word):
                current_dict = self.root
                for letter in word:
                    current_dict = current_dict.setdefault(letter, dict())
                current_dict["_end_"] = True

            def __contains__(self, word):
                current_dict = self.root
                for letter in word:
                    if letter not in current_dict:
                        return False
                    current_dict = current_dict[letter]
                return "_end_" in current_dict

            def __delitem__(self, word):
                current_dict = self.root
                nodes = [current_dict]
                for letter in word:
                    current_dict = current_dict[letter]
                    nodes.append(current_dict)
                del current_dict["_end_"]
        
        
        t = Trie()
        
        for w in wordDict:
            t.add(w)
        
        
        possibility = list()
        answer = []
        
        def explore(start):
                                  
            if start == len(s):
                answer.append(' '.join(possibility))
                return
            
            trie = t.root
                        
            for current in range(start, len(s)):
                char = s[current] 
                if char in trie:
                    if '_end_' in trie[char]:
                        possibility.append(s[start:current + 1])
                        explore(current + 1)
                        possibility.pop()
                    trie = trie[char]
                else:
                    break
                    
        explore(0)       
        
        return answer

#https://leetcode.com/problems/word-break-ii/discuss/44311/Python-easy-to-understand-solution
#fast solution
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, memo):
        if s in memo: return memo[s]
        if not s: return []

        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
                for item in resultOfTheRest:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res