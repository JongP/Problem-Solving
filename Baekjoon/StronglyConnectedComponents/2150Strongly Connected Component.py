import sys
input=lambda : sys.stdin.readline().rstrip()

sys.setrecursionlimit(10**5)

V,E=map(int,input().split())

graph=[[ ] for _ in range(V)]
dfsn=[-1]*V
finished=[0]*V
stk=[]
resList=[]
id=0

for _ in range(E):
    a,b=map(lambda x: int(x)-1,input().split())
    graph[a].append(b)


def dfs(node):
    global id
    dfsn[node] =res= id
    stk.append(node)
    id+=1

    for nextt in graph[node]:
        if dfsn[nextt]==-1:
            res=min(res,dfs(nextt))
        elif finished[nextt]==0:
            res=min(res,dfsn[nextt])
    
    

    if dfsn[node]==res:
        tmpL=[]
        while True:
            t=stk.pop()
            tmpL.append(t+1)
            finished[t]=1
            if t==node:
                 break

        tmpL.sort()
        resList.append(tmpL)
        
    return res

for i in range(V):
    if dfsn[i]==-1:
        dfs(i)

print(len(resList))
resList.sort()

for res in resList:
    for num in res:
        print(num,end=" ")
    print(-1)





