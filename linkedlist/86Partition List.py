# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        sH=sTrav=ListNode()
        lH=lTrav=ListNode()
        
        
        trav=head
        
        while trav:
            if trav.val<x:
                sTrav.next=trav
                sTrav=trav
            else:
                lTrav.next=trav
                lTrav=trav
            
            
            trav=trav.next
        
        #connection
        sTrav.next=lH.next
        lTrav.next=None
            
        return sH.next