# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n=0
        trav=head
        while trav:
            trav=trav.next
            n+=1
            
        
        
        if k>n-k+1:
            k=n-k+1
        #print(k,n-k+1)
        trav=head
        node=None
        for i in range(n-k):
            if i==k-1:
                node=trav
            
            trav=trav.next
        if node:
            node.val,trav.val=trav.val,node.val
        
        return head

#https://leetcode.com/problems/swapping-nodes-in-a-linked-list/discuss/1054370/Python-3-or-Swapping-NODES-or-Swapping-Values-or-One-Pass-or-Fully-explained
#like slidng window or two pointer.  we don't have to calculate n-k+1
def swapNodes(self, head: ListNode, k: int) -> ListNode:
	first = last = head
	for i in range(1, k):
		first = first.next
		
	null_checker = first 
	while null_checker.next:
		last = last.next
		null_checker = null_checker.next
	first.val, last.val = last.val, first.val
	return head

    
def swapNodes(self, head: ListNode, k: int) -> ListNode:
    dummy = pre_right = pre_left = ListNode(next=head)
    right = left = head
    for i in range(k-1):
        pre_left = left
        left = left.next
    
    null_checker = left
    
    while null_checker.next:
        pre_right = right
        right = right.next
        null_checker = null_checker.next
        
    if left == right:
        return head
    
    pre_left.next, pre_right.next = right, left
    left.next, right.next = right.next, left.next
    return dummy.next      