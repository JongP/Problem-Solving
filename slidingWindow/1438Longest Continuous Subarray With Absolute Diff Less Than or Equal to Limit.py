from heapq import heappop,heappush
#hint on sliding window
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l=len(nums)
        le=ri=0
        minV=maxV=nums[0]
        maxHeap=[]
        minHeap=[]
        
        
        cnter=collections.Counter()
        
        
        while ri<l:
            heappush(maxHeap,-nums[ri])
            heappush(minHeap,nums[ri])
            
            #updating heap
            while maxHeap and cnter[-maxHeap[0]]>0:
                cnter[-heappop(maxHeap)]-=1
                
            while minHeap and cnter[minHeap[0]]>0:
                cnter[heappop(minHeap)]-=1
            
            
            while ri+1<l and maxHeap and max(-maxHeap[0],nums[ri+1])-min(minHeap[0],nums[ri+1])<=limit:
                ri+=1
                heappush(maxHeap,-nums[ri])
                heappush(minHeap,nums[ri])
            
            cnter[nums[le]]+=1
            le+=1
            ri+=1
        
        
        
        return ri-le+1