"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy=trav=Node(x=0,next=head)
        hashMap={}
        hashMap[dummy]=Node(x=0)
        
        while trav:
            
            self.copyNode(trav,hashMap,True)
            self.copyNode(trav,hashMap,False)
            
            trav=trav.next
        
        return hashMap[dummy].next
    
    def copyNode(self,node,hashMap,isNext):
            nxtNode= node.next if isNext else node.random
            if not nxtNode: return
            
            
            if nxtNode not in hashMap:
                hashMap[nxtNode]=Node(x=nxtNode.val)
            
            if isNext:
                hashMap[node].next=hashMap[nxtNode]
            else:
                hashMap[node].random=hashMap[nxtNode]