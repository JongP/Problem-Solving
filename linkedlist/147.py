# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur=head.next
        head.next=None
        
        while cur:
            prevNode=None
            trav=head
            tmp=cur.next
            
            while True:
                if cur.val<trav.val:
                    
                    if prevNode:
                        cur.next=prevNode.next
                        prevNode.next=cur
                    else:
                        cur.next=head
                        head=cur
                    break
                prevNode=trav
                trav=trav.next
                if not trav:
                    prevNode.next=cur
                    cur.next=None
                    break
            cur=tmp    
        
        
        return head

#http://steve-yegge.blogspot.nl/2008/03/get-that-job-at-google.html