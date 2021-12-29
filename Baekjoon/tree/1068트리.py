from collections import defaultdict

n=int(input())
arr=list(map(int,input().rstrip().split()))
target=int(input())

graph=defaultdict(list)
inDeg=[0]*n

for i,v in enumerate(arr):
    if v==-1:
        root=i
        continue

    graph[v].append(i)
    inDeg[v]+=1

#delete the target
stk=[target]

while stk:
    cur=stk.pop()
    inDeg[cur]=-1
    for nxt in graph[cur]:
        stk.append(nxt)

inDeg[arr[target]]-=1

print(inDeg.count(0))

