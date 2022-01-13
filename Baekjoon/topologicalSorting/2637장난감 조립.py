#Good Problem
import sys
from collections import defaultdict
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())

N=int(input())
M=int(input())

graph=defaultdict(list)
inDegrees=[0]*N
isPrime=[True]*N
numParts=[0]*N
numParts[N-1]=1

for _ in range(M):
    X,Y,K=map(int,input().split());X-=1;Y-=1;
    graph[X].append((Y,K))
    inDegrees[Y]+=1
    isPrime[X]=False

que=[N-1]

while que:
    cur=que.pop()

    for nextt,nextNum in graph[cur]:
        numParts[nextt]+=nextNum*numParts[cur]
        inDegrees[nextt]-=1
        if inDegrees[nextt]==0:
            que.append(nextt)


for i in range(N):
    if isPrime[i]:
        print(i+1, numParts[i])

