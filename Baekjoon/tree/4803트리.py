from collections import defaultdict
import sys
input=sys.stdin.readline
#map(int,input().rstrip().split())

ansList=[]

def processInput(m):
    g=defaultdict(list)
    for _ in range(m):
        a,b=map(int,input().rstrip().split())
        a-=1;b-=1;
        g[a].append(b)
        g[b].append(a)
    return g

def goDFS(graph,visited,node,parent):
    visited[node]=1

    for nxt in graph[node]:
        if nxt==parent:
            continue
        if visited[nxt]==1:
            return 0
        if not goDFS(graph,visited,nxt,node):
            return 0

    return 1


caseNum=1
while True:
    n,m=map(int,input().rstrip().split())
    if n==0 and m==0:
        break

    visited=[0]*n
    res=0

    graph=processInput(m)
    
    for i in range(n):
        if visited[i]==0:
            res+=goDFS(graph,visited,i,-1)
    
    ansList.append((caseNum,res))
    caseNum+=1



for cnt, res in ansList:
    if res==0:
        print("Case %d: No trees." %cnt)
    elif res==1:
        print("Case %d: There is one tree." %cnt)
    else:
        print("Case %d: A forest of %d trees." %(cnt,res))

