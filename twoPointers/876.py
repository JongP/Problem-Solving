# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=1
        
        trav=head
        while trav.next:
            l+=1
            trav=trav.next
            
        print(l)
        
        for _ in range(l//2):
            head=head.next
        return head