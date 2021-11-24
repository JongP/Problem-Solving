# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fTrav=head
        for _ in range(n):
            fTrav=fTrav.next
        
        if not fTrav:
            return head.next
        
        bTrav=head
        while fTrav.next:
            fTrav=fTrav.next
            bTrav=bTrav.next
        bTrav.next=bTrav.next.next
        
        
        return head
    
    
    def firstRemoveNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        
        
        l=1
        trav=head
        while trav.next:
            trav=trav.next
            l+=1
            
        if l==n:
            return head.next
        
        
        trav=head
        for _ in range(l-n-1):
            trav=trav.next
        trav.next=trav.next.next
        return head
        