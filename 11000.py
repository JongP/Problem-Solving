import heapq
import sys
input = sys.stdin.readline

answer=0
waitingHeap=[]
goingHeap=[]

t=int(input())
for _ in range(t):
    s,e=map(int,input().rstrip().split())
    waitingHeap.append((s,e))
waitingHeap.sort()

for s,e in waitingHeap:
    if not goingHeap or goingHeap[0]>s:
        answer+=1
        heapq.heappush(goingHeap,e)
    else:
        heapq.heappop(goingHeap)
        heapq.heappush(goingHeap,e)

print(answer)