# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        
        
        #trav=head
        subHead=head.next
        subTail=head.next
        prevTrav=head
        trav=head.next.next
        head.next=head.next.next
        
        while trav:
            
            subTail.next=trav.next
            subTail=trav.next
            
            
            trav.next = trav.next.next if trav.next else trav.next
            
            
            prevTrav=trav
            trav=trav.next
            
        
        prevTrav.next=subHead
        
        
        return head
#https://leetcode.com/problems/odd-even-linked-list/discuss/78095/Clear-Python-Solution
    def oddEvenList(self, head):
        dummy1 = odd = ListNode(0)
        dummy2 = even = ListNode(0)
        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            head = head.next.next if even else None
        odd.next = dummy2.next
        return dummy1.next