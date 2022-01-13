import sys
from collections import defaultdict
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())

ansL=[]

for _ in range(int(input())):
    N,K=map(int,input().split())
    costs=list(map(int,input().split()))
    
    times=[0]*N
    graph=defaultdict(list)
    inDegrees=[0]*N

    for _ in range(K):
        a,b=map(lambda x:int(x)-1,input().split())
        inDegrees[b]+=1
        graph[a].append(b)

    target=int(input())-1

    que=[]
    for i in range(N):
        if inDegrees[i]==0:
            que.append(i)
    
    while que:
        cur=que.pop()
        times[cur]+=costs[cur]
        if cur==target:
            ansL.append(times[cur])
            break
        for nextt in graph[cur]:
            times[nextt]=max(times[nextt],times[cur])
            inDegrees[nextt]-=1
            if inDegrees[nextt]==0:
                que.append(nextt)


#DFS
#https://www.acmicpc.net/source/33255272
import sys; readline = sys.stdin.readline

for _ in range(int(readline().rstrip())):
    N, K = map(int,readline().split())
    build_time = [-1]+list(map(int,readline().split()))
    root = [[] for i in range(N+1)]

    for _ in range(K):
        a, b = map(int,readline().split())
        root[b].append(a)

    fin = int(readline().rstrip())
    dp = [-1]*(N+1)
    def recur(node):
        if dp[node] != -1:
            return dp[node]
        time = 0
        for x in root[node]:
            tmp = recur(x)
            time = max(time,tmp)
        dp[node] = time + build_time[node]
        return dp[node]
    recur(fin)
    if dp[fin] == -1:
        print(build_time[fin])
    else:
        print(dp[fin])


[print(a) for a in ansL]