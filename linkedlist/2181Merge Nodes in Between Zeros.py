# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=resTrav=ListNode()
        trav=head.next
        cur=0
        
        while trav:
            if trav.val==0:
                resTrav.next=trav
                resTrav=trav
                trav.val=cur
                cur=0
            else:
                cur+=trav.val    
            trav=trav.next
        
        return dummy.next
    
        