class LinkNode:
    def __init__(self,key=None,val=None,nxt=None,prev=None):
        self.key=key
        self.val=val
        self.nxt=nxt
        self.prev=prev
        
    def debugPrint(self):
        trav=self
        while trav:
            print(trav.key,trav.val)
            trav=trav.nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.head=LinkNode()
        self.tail=LinkNode(nxt=self.head)
        self.head.prev=self.tail
        self.d={}
        self.size=0
        self.cap=capacity
        
    def get(self, key: int) -> int:
        #self.tail.debugPrint()
        if key not in self.d:
            return -1
        node=self.d[key]
        #print(node.prev.val)
        node.prev.nxt=node.nxt
        node.nxt.prev=node.prev
        #self.tail.debugPrint()
        
        node.nxt=self.tail.nxt
        self.tail.nxt.prev=node
        
        node.prev=self.tail
        self.tail.nxt=node
        
        #self.tail.debugPrint()
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.get(key)
            self.d[key].val=value
        else:
            if self.cap==self.size:
                #print(self.d)
                node=self.head.prev
                del self.d[node.key]
                node.prev.nxt=node.nxt
                node.nxt.prev=node.prev
                
                self.size-=1
                
            self.size+=1
            self.d[key]=LinkNode(key=key,val=value)
            
            self.d[key].nxt=self.tail.nxt
            self.tail.nxt.prev=self.d[key]
            
            self.d[key].prev=self.tail
            self.tail.nxt=self.d[key]
        #self.tail.debugPrint()
                    


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



#https://leetcode.com/problems/lru-cache/discuss/45926/Python-Dict-%2B-Double-LinkedList
class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    def set(self, key, value):
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

