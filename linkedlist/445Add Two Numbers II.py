class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        val=self.makeNumber(l1) + self.makeNumber(l2)
        
        return self.makeListNode(val) or ListNode(val=0)
        
        
        
    def makeNumber(self, node):
        res=0
        
        while node:
            res=10*res+node.val
            node=node.next
            
        return res

    def makeListNode(self,num):
        
        prev=None
        
        while num:
            num,val=divmod(num,10)
            prev=ListNode(val=val,next=prev)
            
        return prev

#Stack --> LIFO --> reverse input ouput order
#https://leetcode.com/problems/add-two-numbers-ii/discuss/926807/Python-Two-stacks-solution-explained
class Solution:
    def addTwoNumbers(self, l1, l2):
        st1, st2 = [], []
        while l1:
            st1.append(l1.val)
            l1 = l1.next
            
        while l2:
            st2.append(l2.val)
            l2 = l2.next
        
        carry, head = 0, None

        while st1 or st2 or carry:
            d1, d2 = 0, 0
            d1 = st1.pop() if st1 else 0
            d2 = st2.pop() if st2 else 0
            carry, digit = divmod(d1 + d2 + carry, 10)
            head_new = ListNode(digit)
            head_new.next = head
            head = head_new
              
        return head