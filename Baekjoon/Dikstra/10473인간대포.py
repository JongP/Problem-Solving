#what is diff with **.5 and sqrt
import heapq
from math import sqrt
import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())

def timeToWalk(a,b):
    return (sqrt((a[0]-b[0])**2+(a[1]-b[1])**2))/5

start=tuple(map(float,input().split()))
end=tuple(map(float,input().split()))
nodes=[end]
costs=[timeToWalk(start,end)]
visited=set()
heap=[]
heapq.heappush(heap,(costs[0],0))

n=int(input())
for i in range(n):
    nodes.append(tuple(map(float,input().split())))
    costs.append(timeToWalk(start,nodes[-1]))
    heapq.heappush(heap,(costs[-1],i+1))

while heap:
    cost,node=heapq.heappop(heap)
    if node in visited:
        continue
    
    if node==0:
        print(cost)
        exit()
    visited.add(node)
    
    cx,cy=nodes[node]
    for i, (nx,ny) in enumerate(nodes):
        if i in visited:
            continue
        
        dist=sqrt(((cx-nx)**2+(cy-ny)**2))
        newTime=min(dist/5,2+abs(dist-50)/5)+cost

        if newTime<costs[i]:
            costs[i]=newTime
            heapq.heappush(heap,(newTime,i))






