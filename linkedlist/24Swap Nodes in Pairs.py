# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddHead=oddTrav=ListNode()
        evenHead=evenTrav=ListNode()
        
        #build oddHead and evenHead
        trav=head
        while trav:
            oddTrav.next=trav
            oddTrav=trav
            
            if not trav.next: break
            
            evenTrav.next=trav.next
            evenTrav=trav.next
            trav=trav.next.next
            
        oddTrav.next=evenTrav.next=None
        
        #build res
        oddTrav,evenTrav=oddHead.next,evenHead.next
        res=trav=ListNode()
        
        while evenTrav:
            trav.next=evenTrav
            evenTrav=evenTrav.next
            trav=trav.next
            
            trav.next=oddTrav
            oddTrav=oddTrav.next
            trav=trav.next
        
        trav.next=oddTrav
        
        
        
        
        return res.next


#exmaple

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        top = ListNode(0)
        top.next = head
        
        current = top
        while current.next and current.next.next:
            nnn = current.next.next.next
            nn = current.next.next
            n = current.next
            n.next = nnn
            nn.next = n
            current.next = nn
            current = n
        
        return top.next