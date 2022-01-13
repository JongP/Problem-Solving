import sys
from collections import defaultdict
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())

N,M=map(int,input().split())

inDegrees=[0]*(N+1)#skip the 0th
graph=defaultdict(list)

for _ in range(M):
    line= list(map(int,input().split()))
    #print(line)
    for i in range(1,len(line)-1):
        inDegrees[line[i+1]]+=1
        graph[line[i]].append(line[i+1])

que=[]
res=[]
for i in range(1,N+1):
    if inDegrees[i]==0:
        que.append(i)

while que :
    cur=que.pop()
    res.append(cur)
    for nextt in graph[cur]:
        inDegrees[nextt]-=1
        if inDegrees[nextt]==0:
            que.append(nextt)

if len(res)==N:
    [print(a) for a in res]
else:
    print(0)


