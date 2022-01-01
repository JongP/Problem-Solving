import sys
input=sys.stdin.readline
import heapq
#map(int,input().rstrip().split())
#sys.setrecursionlimit(10**6)
k,n=map(int,input().rstrip().split())
arr=list(map(int,input().rstrip().split()))
visited=set()

heap=arr.copy()
heapq.heapify(heap)

for _ in range(n-1):
    res=heapq.heappop(heap)

    while res in visited:
        res=heapq.heappop(heap)
    visited.add(res)

    for elem in arr:
        if res*elem<(1<<31) and res*elem not in visited:
            heapq.heappush(heap,res*elem)
            #visited.add(res*elem)
res=heapq.heappop(heap)

while res in visited:
    res=heapq.heappop(heap)

print(res)


#https://www.acmicpc.net/source/34073774
import sys
import heapq

k, n = map(int, sys.stdin.readline().split())
prime = list(map(int, sys.stdin.readline().split()))
arr = prime[:]
heapq.heapify(arr)

for _ in range(n - 1):
    p = heapq.heappop(arr)
    for q in prime:
        heapq.heappush(arr, p * q)
        if p % q == 0: #prevent repetition
            break

print(heapq.heappop(arr))
