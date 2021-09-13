import heapq
from collections import deque
import sys
input = sys.stdin.readline

def solution(jobs):
    
    l = len(jobs)
    sum_start = 0
    sum_end = 0
    clock =0 
    heap = []
    heapq.heapify(jobs)

    #assume that jobs is in order of jobs[0] asc
    while jobs or heap:
        if not heap:
            start, progress = heapq.heappop(jobs)
            heapq.heappush(heap,progress)
            sum_start+=start
            clock = start
            continue
        
        cur_progess = heapq.heappop(heap)

        clock+=cur_progess
        sum_end += clock

        while jobs and jobs[0][0]<=clock:
            start, progress = heapq.heappop(jobs)
            heapq.heappush(heap,progress)
            sum_start+=start

    #print(sum_end,sum_start,l)
    return (sum_end-sum_start)//l


print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[0, 3], [4, 3], [10, 3]]))