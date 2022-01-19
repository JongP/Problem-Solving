# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        #O(n), O(n)
        trav=head
        visited=set()
        while trav:
            if trav in visited:
                return trav
            visited.add(trav)      #object variable can be hashed  
            trav=trav.next
            
        return None


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:return None
        turtoise=head.next#I miss-wrote head not head.next
        hares=head.next.next if head.next else None
        
        while hares and turtoise!=hares:
            
            
            
            turtoise=turtoise.next
            hares=hares.next.next if hares.next else None
        
        if not hares:
            return None
        
        hares=head
        while hares!=turtoise:
            hares=hares.next
            turtoise=turtoise.next
        return hares
        
        
