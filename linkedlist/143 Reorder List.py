# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        self.front=head
        def helper(node):
            if not node:
                return True
            
            if helper(node.next):
                if self.front.next==node or self.front==node:
                    node.next=None
                    return False
                
                tmp=self.front
                self.front=self.front.next
                node.next=self.front
                tmp.next=node
                return True
            
            return False
            
        helper(head)

#optimized with stack.
#using stack is cheaper than using recursion.

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stk=[]
        trav=head
        while trav:
            stk.append(trav)
            trav=trav.next
            
        front=head
        while stk and front!=stk[-1] and front.next!=stk[-1]:
            tail=stk.pop()
            tail.next=front.next
            front.next=tail
            front=tail.next
            
            
        if stk:
            stk[-1].next=None




#billiant idea 
#a lot to learn!!
#https://leetcode.com/problems/reorder-list/discuss/44988/A-python-solution-O(n)-time-O(1)-space
    # Splits in place a list in two halves, the first half is >= in size than the second.
    # @return A tuple containing the heads of the two halves
    def _splitList(head):
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            fast = fast.next

        middle = slow.next
        slow.next = None

        return head, middle

    # Reverses in place a list.
    # @return Returns the head of the new reversed list
    def _reverseList(head):

    last = None
    currentNode = head

    while currentNode:
        nextNode = currentNode.next
        currentNode.next = last
        last = currentNode
        currentNode = nextNode

    return last

    # Merges in place two lists
    # @return The newly merged list.
    def _mergeLists(a, b):

        tail = a
        head = a

        a = a.next
        while b:
            tail.next = b
            tail = tail.next
            b = b.next
            if a:
                a, b = b, a
                
        return head


    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):

        if not head or not head.next:
            return

        a, b = _splitList(head)
        b = _reverseList(b)
        head = _mergeLists(a, b)