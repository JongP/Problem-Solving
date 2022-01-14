import sys
input=lambda : sys.stdin.readline().rstrip()

sys.setrecursionlimit(10**5)

N,M=map(int,input().split())
graph=[[] for _ in range(N)]


for _ in range(M):
    a,b=map(lambda x: int(x)-1,input().split())
    graph[a].append(b)

moneys=[int(input()) for _ in range(N)]

S,P=map(int,input().split());S-=1

restaurants=set(map(int,input().split()))


#SCC
id=0
sn=-1
dfsn=[-1]*N
finished=[0]*N
sccNums=[-1]*N
sccSums=[]
stk=[]

def dfs(node):
    global id,sn
    dfsn[node]=id;id+=1
    stk.append(node)


    res=dfsn[node]
    for nextt in graph[node]:
        if dfsn[nextt]==-1:
            res=min(res,dfs(nextt))
        elif finished[nextt]==0:
            res=min(res,dfsn(nextt))
    
    if dfsn[node]==res:
        sn+=1
        sccSum=0
        while True:
            tmp=stk.pop()
            sccNums[tmp]=sn
            sccSum+=moneys[tmp]
            if tmp==node:
                break
        sccSums.append(sccSum)

    return res

for i in range(N):
    if dfsn[i]==-1:
        dfs(i)

#build graph for  topological sorting
sccGraph=[set() for _ in range(sn+1)]
inDegrees=[0]*(sn+1)
sccRes=set()

for i in range(N):
    if i==S:
        sccS=sccNums[i]
    if i in restaurants:
        sccRes.add(sccNums[i])
    

    for j in graph[i]:
        if sccNums[i]!=sccNums[j]:
            if sccNums[j] not in sccGraph[sccNums[i]]:
                sccGraph[sccNums[i]].add(sccNums[j])
                inDegrees[sccNums[j]]+=1


#topological sorting
resL=[0]*(sn+1)
stk=[]

#for i in range(sn+1):
#    if inDegrees[i]==0:
#        stk.append(i)
stk.append(sccS)

while stk:
    cur=stk.pop()
    resL[cur]+=sccSums[cur]

    for nextt in sccGraph[cur]:
        inDegrees[nextt]-=1
        if inDegrees[nextt]==0:
            stk.append(nextt)

        resL[nextt]+=resL[cur]
res=0
for r in sccRes:
    res=max(res,resL[r])

print(res)
