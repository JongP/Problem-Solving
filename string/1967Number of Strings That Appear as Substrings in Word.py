class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        res=0
        
        for p in patterns:
            if p in word:res+=1
                
        return res
#one line
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(p in word for p in patterns)


#Aho–Corasick Algorithm
#https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/discuss/1404687/Python-AhoCorasick-Algorithm-KMP-%2B-Trie-O(N-%2B-M)
class Node:
    def __init__(self, val):
        self.val = val
        self.next = dict()
        self.end = 0
        self.fail = None
        self.used = False

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        root = Node('ROOT')
        for pattern in patterns:
            node = root
            for x in pattern:
                if x not in node.next:
                    node.next[x] = Node(x)
                node = node.next[x]
            node.end += 1
            
        queue = collections.deque([root])
        while queue:
            pnode = queue.popleft()
            for x, nnode in pnode.next.items():
                if pnode == root:
                    nnode.fail = pnode
                else:
                    ptr = pnode.fail
                    while ptr != root and x not in ptr.next:
                        ptr = ptr.fail
                    if x in ptr.next:
                        ptr = ptr.next[x]
                    nnode.fail = ptr
                queue.append(nnode)
        
        res = 0
        ptr = root
        for x in word:
            while ptr != root and x not in ptr.next:
                ptr = ptr.fail
            if x in ptr.next:
                ptr = ptr.next[x]
            tmp = ptr
            while tmp != root and tmp.used == False:
                res += tmp.end
                tmp.used = True
                tmp = tmp.fail
                
        return res