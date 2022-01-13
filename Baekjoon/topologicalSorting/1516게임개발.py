import sys
from collections import defaultdict
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())

n=int(input())
times=[0]*n
inDegrees=[0]*n
graph=defaultdict(list)

for i in range(n):
    line=list(map(int,input().split()))

    times[i]=line[0]
    for j in range(1,len(line)-1):
        inDegrees[i]+=1
        graph[line[j]-1].append(i)

que=[]
res=[0]*n

for i in range(n):
    if inDegrees[i]==0:
        que.append(i)

while que:
    cur=que.pop()
    res[cur]+=times[cur]

    for nextt in graph[cur]:
        inDegrees[nextt]-=1
        res[nextt]=max(res[nextt],res[cur])
        if inDegrees[nextt]==0:
            que.append(nextt)

[print(a) for a in res]