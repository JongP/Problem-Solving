class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        
        last,n = self.getLastLen(head)
        tail=self.getKth(head,n-k%n)
        
        last.next=head
        head=tail.next
        tail.next=None
        
        return head
    
    def getLastLen(self,head):
        trav=head
        n=1
        while trav.next:
            n+=1
            trav=trav.next
        
        return trav,n
    
    def getKth(self,head,k):
        k-=1
        while k:
            head=head.next
            k-=1
        return head

class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next: return head
        
        last, n = head, 1
        while last.next:
            last = last.next
            n += 1
            
        if k % n == 0: return head
        
        middle = head
        for i in range(n - k%n-1):
            middle = middle.next
            
        new_head = middle.next
        last.next = head
        middle.next = None
        return new_head