# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=cur=ListNode(next=head)
        trav=cur.next
        
        while trav:
            if trav.next and trav.val==trav.next.val:
                val=trav.val
                while trav and trav.val==val: trav=trav.next
            else:
                cur.next=trav
                cur=trav
                trav=trav.next
        
        cur.next=None
            
            
            
        return dummy.next