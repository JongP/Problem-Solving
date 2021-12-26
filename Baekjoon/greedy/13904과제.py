import sys
import heapq
input=sys.stdin.readline

n=int(input())
heap=[]
res=0
task=[]
for _ in range(n):
    task.append(list(map(int,input().rstrip().split())))
task.sort()

day=task[-1][0]

#print(task)

while day>=1:
    #fill the task available
    while task and task[-1][0]>=day:
        heapq.heappush(heap,-1*task.pop()[1])

    if heap:
        res+=-1*heapq.heappop(heap)


    day-=1

print(res)


#https://www.acmicpc.net/source/31387092
hw = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(n)], key=lambda x: (-x[1], x[0]))

#https://www.acmicpc.net/source/28005846
import heapq
import sys
input = sys.stdin.readline

n = int(input())

li = []
for _ in range(n):
    d, r = map(int, input().split())
    li.append((d, r))

li.sort(key=lambda x: x[0])

heap = []
for d, r in li:
    heapq.heappush(heap, r)  
    if len(heap) > d:
        heapq.heappop(heap)

print(sum(heap))