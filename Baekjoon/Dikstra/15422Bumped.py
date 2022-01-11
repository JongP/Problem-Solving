from collections import defaultdict
import heapq
import math
import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())

n,m,f,s,t=map(int,input().split())
roads=defaultdict(list)
flights=defaultdict(list)

for _ in range(m):
    a,b,c=map(int,input().split())
    roads[a].append((b,c))
    roads[b].append((a,c))

for _ in range(f):
    a,b=map(int,input().split())
    flights[a].append(b)



def dikstra(start):
    dists=[math.inf]*n
    dists[start]=0

    heap=[]
    heapq.heappush(heap,(0,start))

    while heap:
        cD,cN=heapq.heappop(heap)
        if dists[cN]<cD:
            continue
        for nextt,cost in roads[cN]:
            if dists[nextt]>cD+cost:
                dists[nextt]=cD+cost
                heapq.heappush(heap,(dists[nextt],nextt))
    return dists

d1=dikstra(s)
d2=dikstra(t)
res=d1[t]

for a in flights:
    for b in flights[a]:
        if res>d1[a]+d2[b]:
            res=d1[a]+d2[b]

print(res)





#with dp
#https://www.acmicpc.net/source/20221149
#https://kscodebase.tistory.com/66
from heapq import heappop, heappush
import sys,math  
input = sys.stdin.readline
inf = math.inf

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dijkstra(n, start, graph, flight):
  d = [ [inf for _ in range(n)] for _ in range(2)]
  d[0][start] = 0 
  q = []
  heappush(q, [0, start, 0])

  while q:

    _, c_pos, f = heappop(q)

    for n_cost, n_pos in graph[c_pos]:
      if d[f][n_pos] > d[f][c_pos] + n_cost:
        d[f][n_pos] = d[f][c_pos] + n_cost
        heappush(q, [d[f][n_pos], n_pos, f])
    
    if f == 0:
      for n_pos in flight[c_pos]:
        if d[1][n_pos] > d[0][c_pos]:
          d[1][n_pos] = d[0][c_pos]
          heappush(q, [d[1][n_pos], n_pos, 1])

  return d    

    
n, m, f, s, t = map(int, input().split())
graph = [ [] for _ in range(n)]
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append([c,b])
  graph[b].append([c,a])
flight = [ [] for i in range(n)]
for _ in range(f):
  a, b = map(int, input().split())
  flight[a].append(b)

d = dijkstra(n, s, graph, flight)
#print(d)
print(min(d[0][t], d[1][t]))