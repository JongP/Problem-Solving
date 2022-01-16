#문제 조건 더 알고 싶음.. good bye
from collections import defaultdict
import sys
input=lambda : sys.stdin.readline().rstrip()

sys.setrecursionlimit(10**5)


def dfs(node):
    global id,sn
    dfsn[node]=id
    id+=1
    stk.append(node)

    parent=dfsn[node]

    for nextt in graph[node]:
        if dfsn.get(nextt,-1)==-1:
            parent=min(parent,dfs(nextt))
        elif dfsn[nextt]!=-2:
            parent=min(parent,dfsn[nextt])
    
    if dfsn[node]==parent:
        tmpSet=set()
        while True:
            t=stk.pop()
            dfsn[t]=-2
            tmpSet.add(t)
            sccNums[t]=sn
            if t==node:
                break
        sccL.append(tmpSet)
        sn+=1

    return parent

N=int(input())
graph=defaultdict(set)
nodes=set()

for _ in range(N):
    line=input().split()
    nodes.add(line[0])
    for prev in line[2:]:
        nodes.add(prev)
        graph[prev].add(line[0])


id=sn=0
sccNums={}
sccL=[]
dfsn={}
stk=[]

for node in nodes:
    if dfsn.get(node,-1)==-1:
        dfs(node)

sccGraph=[set() for _ in range(sn)]
target=input()
res=defaultdict(int)

inDegrees=defaultdict(int)
for node in nodes:
    for nextt in graph[node]:
        inDegrees[nextt]+=1

que=[]
for node in nodes:
    if inDegrees[node]==0:
        que.append(node)





print(res[target])