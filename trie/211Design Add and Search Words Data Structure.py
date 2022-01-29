class WordDictionary:
#I  came up wiht bfs even though I didnt recognize it. 
#but dfs implementation is much more simple.
    def __init__(self):
        self.trie={}
        

    def addWord(self, word: str) -> None:
        trav=self.trie
        for ch in word:
            if ch not in trav: trav[ch]={}
            trav=trav[ch]
        trav["*"]={}
        

    def search(self, word: str) -> bool:
        
        def dfs(word,idx,trav) -> bool:
            if idx==len(word):
                return "*" in trav
            
            if word[idx]==".":
                for nxt in trav:
                    if nxt=="*": continue
                    if dfs(word,idx+1,trav[nxt]): return True
                return False
            elif word[idx] not in trav: return False
            else : return dfs(word,idx+1,trav[word[idx]])
                
                
            
            
        return dfs(word,0,self.trie)

"""
https://leetcode.com/problems/design-add-and-search-words-data-structure/discuss/774530/Python-Trie-solution-with-dfs-explained
Complexity: Easy part is space complexity, it is O(M), where M is sum of lengths of all words in our Trie. 
This is upper bound: in practice it will be less than M and it depends, how much words are intersected. 
The worst time complexity is also O(M), potentially we can visit all our Trie, if we have pattern like ...... 
For words without ., time complexity will be O(h), where h is height of Trie. 
For words with several letters and several ., we have something in the middle.
"""


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)