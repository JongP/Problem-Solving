# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #if not head.next:
        #    return None
        
        dummy=ListNode(next=head)
        prevS=dummy
        slow=fast=head
        
        while fast and fast.next:
            fast=fast.next.next
            prevS=slow
            slow=slow.next
        
        prevS.next=slow.next
        
        
        
        return dummy.next