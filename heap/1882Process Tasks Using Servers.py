from heapq import heappop,heappush
from collections import deque
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        #freeHeap  [weight, index]
        #onGoingHeap (endtime, index)
        #que --> task que
        
        #iterating tasks
        # onGoingHeap-->freeHeap
        # task->que
        # que+freeHeap --> onGoingHeap
        
        freeHeap= self.initHeap(servers)
        ongoingHeap=[]
        que=deque()
        ans=[-1]*len(tasks)
        cnt=0
        
            

        #do the last tasks
        cur=-1
        while cnt!=len(tasks):
            if cur<len(tasks)-1:
                cur+=1
            else:
                cur=ongoingHeap[0][0]
            
            
            while ongoingHeap and ongoingHeap[0][0]==cur:
                _,sIdx=heappop(ongoingHeap)
                heappush(freeHeap,(servers[sIdx],sIdx))
                
            if cur<len(tasks):
                que.append((cur,tasks[cur]))

            while freeHeap and que:
                _,sIdx = heappop(freeHeap)
                tIdx,task=que.popleft()
                heappush(ongoingHeap,(cur+task,sIdx  ))
                ans[tIdx]=sIdx
                cnt+=1
            
        return ans
        
    def initHeap(self,servers):
        heap=[]
        
        for i,v in enumerate(servers):
            heappush(heap,(v,i))
        
        
        return heap


#https://leetcode.com/problems/process-tasks-using-servers/discuss/1239767/Python-3-Simulation-Heap-Solution
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        res = []
        h1 = [[weight, i ,0] for i, weight in enumerate(servers)]
        h2 = []
        heapq.heapify(h1)
        for j, task in enumerate(tasks):
            while h2 and h2[0][0] <= j or not h1:
                time, weight, i = heapq.heappop(h2)
                heapq.heappush(h1, [weight, i, time])
            weight, i, time = heapq.heappop(h1)
            res.append(i)
            heapq.heappush(h2, [max(time,j)+task, weight, i])
        return res