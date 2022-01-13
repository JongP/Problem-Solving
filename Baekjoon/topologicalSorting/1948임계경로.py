import sys
from collections import defaultdict
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())


n=int(input())
m=int(input())

graph=[[ ] for _ in range(n)]
backGraph= [[ ] for _ in range(n)]
maxTimes=[0]*n
inDegrees=[0]*n

for _ in range(m):
    a,b,c=map(int,input().split());a-=1;b-=1;
    graph[a].append((b,c))
    inDegrees[b]+=1

start,end=map(lambda x:int(x)-1,input().split())

que=[start]

while que:
    cur=que.pop()

    for nextt,cost in graph[cur]:
        inDegrees[nextt]-=1
        if inDegrees[nextt]==0:
            que.append(nextt)
        
        if maxTimes[nextt]<maxTimes[cur]+cost:
            maxTimes[nextt]=maxTimes[cur]+cost
            backGraph[nextt].clear()
            backGraph[nextt].append(cur)
        elif maxTimes[nextt]==maxTimes[cur]+cost:
            backGraph[nextt].append(cur)

print(maxTimes[end])

que=[end]
visited=[False]*n
res=0

while que:
    cur=que.pop()

    for nextt in backGraph[cur]:
        if not  visited[nextt]:
            visited[nextt]=True
            que.append(nextt)
        #print(cur,nextt)
        res+=1

print(res)


