from collections import defaultdict
import sys
input=sys.stdin.readline

sys.setrecursionlimit(10**5)
#map(int,input().rstrip().split())

n=int(input())
populations=list(map(int,input().rstrip().split()))
graph=defaultdict(list)
visited=[0]*n

for _ in range(n-1):
    a,b=map(int,input().rstrip().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)


def getMax(node):
    visited[node]=1

    childNum=0
    tmp=[]
    for child in graph[node]:
        if visited[child]==1:
            continue
        childNum+=1
        tmp.append(getMax(child))
    
    if childNum==0:
        return (populations[node],0)

    res1=0
    res2=0
    for t in tmp:
        res1+=t[0]
        res2+=t[1]
    
    return (max(res1,res2+populations[node]),res1)




print(max(getMax(0)))


