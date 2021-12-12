import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l=len(nums)
        heap=[]
        
        for i in range(k):
            heapq.heappush(heap,nums[i])            
            
        for i in range(k,l):
            if heap[0]<nums[i]:
                heapq.heappop(heap)
                heapq.heappush(heap,nums[i])

        return heap[0]