class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans=0
        
        while head:
            ans<<=1
            ans+=head.val
            head=head.next
            
        return ans
        
    def getDecimalValue(self, head: ListNode) -> int:
        
        result = 0
        while head:
            result<<=1
            result|=head.val
            head=head.next
        return result
        