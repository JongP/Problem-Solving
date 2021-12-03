# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 or not list2:
            return list1 or list2
        
        dummy=ListNode()
        trav=dummy
        
        while trav:
            if not list1:
                trav.next=list2
                break
            if not list2:
                trav.next=list1
                break
            
            if list1.val<list2.val:
                trav.next=list1
                trav=list1
                list1=list1.next
            else:
                trav.next=list2
                trav=list2
                list2=list2.next
        
        
        
            
            
        return dummy.next
            