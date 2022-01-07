import random
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.arr=[]
        trav=head
        while trav:
            self.arr.append(trav.val)
            trav=trav.next

    def getRandom(self) -> int:
        idx=random.randrange(len(self.arr))
        return self.arr[idx]

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()


#reservoir sampling
#https://leetcode.com/problems/linked-list-random-node/discuss/956872/Python-Reservoir-sampling-(follow-up)-explained

class Solution:
    def __init__(self, head):
        self.head = head

    def getRandom(self):
        n, k = 1, 1
        head, ans = self.head, self.head
        while head.next:
            n += 1
            head = head.next
            if random.random() < k/n:
                ans = ans.next
                k += 1
                
        return ans.val