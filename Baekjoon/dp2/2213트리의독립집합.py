#almost from blog
#https://blog.naver.com/PostView.naver?blogId=kks227&logNo=220793134705&categoryNo=299&parentCategoryNo=0&viewDate=&currentPage=2&postListTopCurrentPage=&from=postList&userTopListOpen=true&userTopListCount=30&userTopListManageOpen=false&userTopListCurrentPage=2
from collections import defaultdict
import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())
#sys.setrecursionlimit(10**5)


n=int(input())
weights=list(map(int,input().split()))
graph=defaultdict(list)
child=defaultdict(list)
for _ in range(n-1):
    a,b=map(lambda x:int(x)-1,input().split())
    graph[a].append(b)
    graph[b].append(a)

#make tree
visited=[0]*n
def makeTree(node):
    visited[node]=1
    for nxt in graph[node]:
        if visited[nxt]==0:
            child[node].append(nxt)
            makeTree(nxt)
makeTree(0)#root is 0

#get max set value
dp=[[-1]*2 for _ in range(n)]
picked=[[-1]*2 for _ in range(n)]
def getMaxSet(node,prev):
    if dp[node][prev]!=-1:
        return dp[node][prev]
    
    noPick=0
    pick=int(-1*2e9)
    for ch in child[node]:
        noPick+=getMaxSet(ch,False)

    
    if not prev:
        pick=weights[node]
        for ch in child[node]:
            pick+=getMaxSet(ch,True)

    dp[node][prev]=max(noPick,pick)
    picked[node][prev]=0 if noPick>pick else 1

    return dp[node][prev]


val=getMaxSet(0,False)
res=[]

def getNodes(node,prev):
    if picked[node][prev]==1:
        res.append(node+1)
        for ch in child[node]:
            getNodes(ch,True)
    else:
        for ch in child[node]:
            getNodes(ch,False)


getNodes(0,False)

res.sort()
print(val)
print(" ".join(map(str,res)))