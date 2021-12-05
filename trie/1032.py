class Node:
    def __init__(self,val=None):
        self.val=val
        self.child={}

class Trie:
    def __init__(self):
        self.head=Node()
    
    def insert(self,chars):
        cur=self.head
        
        for char in chars:
            if char not in cur.child:
                cur.child[char]=Node(char)
            cur=cur.child[char]
        cur.child['*']=Node('*')
    
    def search(self,chars):
        cur=self.head
        
        for char in chars:
            if char not in cur.child:
                return False
            cur=cur.child[char]
        if '*' in cur.child:
            return True
            
    def nextNode(self,node,ch):
        if ch not in node.child:
            return None
        
        node=node.child[ch]
        return node
        
        
class StreamChecker:
    
    def __init__(self, words: List[str]):
        self.trie=Trie()
        for word in words:
            self.trie.insert(word)
        self.cands=[]

    def query(self, letter: str) -> bool:
        ans=False
        tmp=[]
        for cand in self.cands:
            if letter not in cand.child:
                continue
            trav= cand.child[letter]
            if '*' in trav.child:
                ans=True
            tmp.append(trav)
        
        if letter in self.trie.head.child:   
            cur= self.trie.head.child[letter]
            if '*' in cur.child:
                ans=True
            tmp.append(cur)
        
        self.cands=tmp
        
        return ans
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)



#https://leetcode.com/problems/stream-of-characters/discuss/320837/Easily-implemented-Python-Trie-Solution
class TrieNode():
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

class StreamChecker:
    def __init__(self, words: List[str]):
        self.letters = []
        self.trie = Trie()
        for w in words:
            self.trie.insert(w[::-1])
        
    def query(self, letter: str) -> bool:
        self.letters.append(letter)
        i = len(self.letters) - 1
        node = self.trie.root
        while i >= 0:
            if node.isEnd:
                return True
            if self.letters[i] not in node.children:
                return False
            node = node.children[self.letters[i]]
            i -= 1
        return node.isEnd


class StreamChecker:

    def __init__(self, words: List[str]):
        self.stream = deque([])
        self.trie = {}
        
        for word in set(words):
            node = self.trie
            for c in word[::-1]:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['$'] = word
            
    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        node = self.trie
        for c in self.stream:
            if '$' in node:
                return True
            if c not in node:
                return False
            node = node[c]
        return '$' in node
