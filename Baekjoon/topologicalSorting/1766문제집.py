import sys
from collections import defaultdict
from heapq import heappush, heappop
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())


N,M=map(int,input().split())
inDegrees=[0]*N
graph=defaultdict(list)
heap=[]

for _ in range(M):
    A,B=map(lambda x:int(x)-1,input().split())
    inDegrees[B]+=1
    graph[A].append(B)

for i in range(N):
    if inDegrees[i]==0:
        heappush(heap,i)


res=[]

while heap:
    cur=heappop(heap)
    res.append(str(cur+1))

    for nextt in graph[cur]:
        inDegrees[nextt]-=1
        if inDegrees[nextt]==0:
            heappush(heap,nextt)

print(" ".join(res))