from collections import defaultdict,deque
from heapq import heappush, heappop

#monotonic que

#hint from leetcode
#you dont have to fix the size of deque!
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        que=deque()
        
        for i in range(k):
            while que and que[-1][0]<nums[i]:
                que.pop()
            que.append((nums[i],i))
        
        res.append(que[0][0])
        
        for i in range(1,len(nums)-k+1):
            if que[0][1]<i: que.popleft()
            
            while que and que[-1][0]<nums[i+k-1]:
                que.pop()
            que.append((nums[i+k-1],i+k-1))
            
            res.append(que[0][0])
        
        return res

#https://leetcode.com/problems/sliding-window-maximum/discuss/598751/JavaPython-MaxHeap-and-BST-and-Decreasing-Deque-Solutions-Clean-code
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dq = deque([])  # store index of `nums` elements, elements is in decreasing order, the front is the maximum element.
        ans = []
        for i in range(n):
            # Eliminate elements less or equal to nums[i]
            while dq and nums[dq[-1]] <= nums[i]: dq.pop()  
                
            # Push index of current nums[i] to the deque
            dq.append(i)
            
            # if reach enough range size k -> add the result
            if i + 1 >= k: ans.append(nums[dq[0]])
            
            # Remove the last element of range size k
            if i - dq[0] + 1 >= k: dq.popleft()
        return ans



#first inefficient solution
#o(nlogn)  --> should be opimized
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        def initInput(nums,k):
            heap=[]
            d=defaultdict(int)
            
            for i in range(k):
                heappush(heap,-1*nums[i])
            
            return heap,d
        
        
        heap,d=initInput(nums,k)
        res=[]
        res.append(-1*heap[0])
        #le=i ri=le+k-1
        for i in range(1,len(nums)-k+1):
            d[nums[i-1]]+=1
            heappush(heap,-1*nums[i+k-1])
            
            while d[-1*heap[0]]>0:
                d[-1*heap[0]]-=1
                heappop(heap)
        
            res.append(-1*heap[0])
        
        return res
