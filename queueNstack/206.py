# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        stk=[]
        
        while head:
            stk.append(head)
            head=head.next
        
        trav=head=stk.pop()
        while stk:
            nextNode=stk.pop()
            trav.next=nextNode
            trav=nextNode
        trav.next=None
        return head
        