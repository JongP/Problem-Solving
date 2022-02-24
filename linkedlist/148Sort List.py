#quick sort
class Solution:
    
    def qSort(self,head) -> tuple:
        if not head:
            return None,None
        
        fH=fTrav=ListNode()
        bH=bTrav=ListNode()
        
        #partition
        trav=head.next
        while trav:
            if trav.val<=head.val:
                fTrav.next=trav
                fTrav=trav
            else:
                bTrav.next= trav
                bTrav=trav
                
            trav=trav.next
            
            
        fTrav.next=None
        bTrav.next=None
        
        
        #sort
        fH,fT = self.qSort(fH.next)
        bH,bT = self.qSort(bH.next)
            
            
        #merge
        if not fT:
            fH=head
        else:
            fT.next=head
        
        if bH:
            head.next=bH
        else:
            bT=head
            head.next=None
            
        
        
        return fH,bT
            
        
        
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.qSort(head)[0]


#merge sort
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def mSort(self,head):
        if not head:
            return None
        elif not head.next:
            return head
        
        slower=faster=head
        
        #partition
        while faster.next and faster.next.next:
            faster=faster.next.next
            slower=slower.next
        
        
        #sort
        node1 = self.mSort(slower.next)
        slower.next=None
        node2 = self.mSort(head)
            
            
        #merge
        dummy=trav=ListNode()
        
        while node1 and node2:
            if node1.val<node2.val:
                trav.next=node1
                trav=node1
                node1=node1.next
            else:
                trav.next=node2
                trav=node2
                node2=node2.next
                
        
        trav.next= node1 or node2
                
        
        return dummy.next
            
        
        
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.mSort(head)



#
class Solution:
    def sortList(self, head):
        if not head or not head.next: return head
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)
    
    def getMid(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid
    
    def merge(self, head1, head2):
        dummy = tail = ListNode(None)
        while head1 and head2:
            if head1.val < head2.val:
                tail.next, tail, head1 = head1, head1, head1.next
            else:
                tail.next, tail, head2 = head2, head2, head2.next
    
        tail.next = head1 or head2
        return dummy.next
# Follow up question askes us to do it in O(1) memory, and it is possible to do it, using bottom-up merge sort, which is much more difficult to implement during interview limits. What I expect that if you just explain the idea, without implementing this will be already quite good. So, idea is the following: imagine, that we have list a1, a2, a3, a4, a5, a6, a7, a8. Let us first sort values in pairs:
# (a1, a2), (a3, a4), (a5, a6), (a7, a8).
# then we sort values in groups by 4, mergin our pairs:
# (a1, a2, a3, a4), (a5, a6, a7, a8).
# And finally we merge them in one group of 9.