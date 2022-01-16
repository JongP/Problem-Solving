#unsolved
import sys
input=lambda : sys.stdin.readline().rstrip()

sys.setrecursionlimit(1000000)

N,M=map(int,input().split())
graph=[[] for _ in range(N)]


for _ in range(M):
    a,b=map(lambda x: int(x)-1,input().split())
    graph[a].append(b)


moneys=[int(input()) for _ in range(N)]

S,P=map(int,input().split());S-=1

restaurants=set(map(lambda x:int(x)-1,input().split()))


#SCC
id=0
sn=-1
dfsn=[-1]*N
sccNums=[-1]*N
sccSums=[]

sccRes=set()
stk=[]

def dfs(node):
    global id,sn
    dfsn[node]=id;id+=1
    stk.append(node)


    res=dfsn[node]
    for nextt in graph[node]:
        if dfsn[nextt]==-1:
            res=min(res,dfs(nextt))
        elif dfsn[nextt]!=-2:
            res=min(res,dfsn[nextt])
    
    if dfsn[node]==res:
        sn+=1
        sccSum=0
        while True:
            tmp=stk.pop()
            sccNums[tmp]=sn
            sccSum+=moneys[tmp]
            dfsn[tmp]=-2#if we don't have this


            if tmp==node:
                break
        sccSums.append(sccSum)

    return res

for i in range(N):
    if dfsn[i]==-1:
        dfs(i)

#build graph for  topological sorting
sccGraph=[[] for _ in range(sn+1)]
sccS=sccNums[S]
inDegrees=[0]*(sn+1)


for i in range(N):
        if i in restaurants:
            sccRes.add(sccNums[i])
        for nextt in graph[i]:
            if sccNums[i]!=sccNums[nextt] :
                sccGraph[sccNums[i]].append((sccNums[nextt]))
                inDegrees[sccNums[nextt]]+=1



#topological sorting
reachable=[False]*(sn+1)
reachable[sccS]=True
stk=[]
for i in range(sn+1):
    if inDegrees[i]==0:
        stk.append(i)

resL=[0]*(sn+1)
resL[sccS]=sccSums[sccS]

while stk:
    cur=stk.pop()

    for nextt in sccGraph[cur]:
        inDegrees[nextt]-=1
        if inDegrees[nextt]==0:
            stk.append(nextt)

        if reachable[cur]:
            reachable[nextt]=True
            resL[nextt]=max(resL[nextt],resL[cur]+sccSums[nextt])

res=0
for r in sccRes:
    res=max(res,resL[r])

print(res)