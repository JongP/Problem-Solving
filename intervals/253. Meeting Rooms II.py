from heapq import heappop, heappush
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap=[]
        
        res=1
        for s,e in intervals:
            while heap and heap[0]<=s:
                heappop(heap)
            heappush(heap,e)
            
            if len(heap)>res: res=len(heap)
            
            
        return res
            
        
#brilliant idea
#https://leetcode.com/problems/meeting-rooms-ii/discuss/278270/JavaC%2B%2BPython-Sort-All-Time-Point
    def minMeetingRooms(self, intervals):
        res = cur = 0
        for i, v in sorted(x for i,j in intervals for x in [[i, 1], [j, -1]]):
            cur += v
            res = max(res, cur)
        return res

#https://leetcode.com/problems/meeting-rooms-ii/discuss/67917/Python-heap-solution-with-comments.
    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda x:x.start)
        heap = []  # stores the end time of intervals
        for i in intervals:
            if heap and i.start >= heap[0]: 
                # means two intervals can use the same room
                heapq.heapreplace(heap, i.end)
            else:
                # a new room is allocated
                heapq.heappush(heap, i.end)
        return len(heap)