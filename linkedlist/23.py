import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy=ListNode()
        trav=dummy
        
        flag=True
        
        while flag:
            flag=False
            tmpI,tmpV= -1, None
            for i,v in enumerate(lists):
                if not v:
                    continue
                flag=True
                if tmpI==-1:
                    tmpI,tmpV=i,v
                elif tmpV.val>v.val:
                    tmpI,tmpV=i,v
                    
            if flag:
                #print(tmpI,tmpV.val)
                trav.next=tmpV
                trav=trav.next
                lists[tmpI]=lists[tmpI].next
                
        
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy=ListNode()
        trav=dummy
        
        flag=True
        heap=[]
        
        for i,v in enumerate(lists):
            if not v:
                continue
            heapq.heappush(heap,(v.val,i))

        
        
        while heap:
            v,i = heapq.heappop(heap)
            
            trav.next=lists[i]
            trav=trav.next
            
            lists[i]=lists[i].next
            if lists[i]:
                heapq.heappush(heap,(lists[i].val,i))
            
            
               
        
        
        return dummy.next