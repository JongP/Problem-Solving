# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #O(n) but too expensive space
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def helper(tail,trav,depth):
            if not trav:
                return (None,None)
            
            if depth==k:
                tail.next=trav
                return (trav,trav.next)
            
            n,cache=helper(tail,trav.next,depth+1)
            if n==None:
                return (None,None)
            
            n.next=trav
            
            if depth==1:
                trav.next=cache
            return trav,cache
        
        dummy=ListNode()
        dummy.next=head
        trav=dummy
        
        while True:
            n,c=helper(trav,trav.next,1)
            if n==None:
                break
            trav=n
        
        
        return dummy.next

#brilliant solution. look how to use recursion
#https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/11676/64ms-python-solution1
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        tail = head
        for i in range(k):
            if not tail:
                return head

            tail = tail.next

        tail = self.reverseKGroup(tail, k) #this is important. let's reverse from tail!

        #look how to reverse it with head and tail
        for i in range(k):
            next = head.next
            head.next = tail
            tail = head
            head = next

        return tail

#https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/11653/Python-recursive-and-iterative-solutions-with-comments.
# Recursively
def reverseKGroup(self, head, k):
    if k <= 1 :
        return head
    node, cur = None, head
    #this is quite well-known!
    for _ in xrange(k):
        nxt = cur.next
        cur.next = node
        node = cur
        cur = nxt
    #have to keep in mind this above    
    head.next = self.reverseKGroup(cur, k)
    return node

# Iteratively    
def reverseKGroup(self, head, k):
    if not head or not head.next or k <= 1:
        return head

    dummy = pre = ListNode(0)
    dummy.next = head
    # totally l//k groups, l is number of nodes
    for i in xrange(l//k):
        # reverse each group
        node = None
        for j in xrange(k-1):
            nxt = head.next
            head.next = node
            node = head
            head = nxt
        # update nodes and connect nodes
        tmp = head.next
        head.next = node
        pre.next.next = tmp
        tmp1 = pre.next
        pre.next = head
        head = tmp
        pre = tmp1
    return dummy.next