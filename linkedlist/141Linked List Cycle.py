class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next or not head.next.next: return False
        
        slower,faster=head.next,head.next.next
        
        while faster.next and faster.next.next:
            if slower==faster: return True
            slower=slower.next
            faster=faster.next.next
            
            
        return False
        