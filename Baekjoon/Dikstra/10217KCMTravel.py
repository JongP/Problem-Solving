
from collections import defaultdict,deque
from heapq import heappush,heappop
import math;INF=math.inf
import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())ㅋ


for _ in range(int(input())):
    N,M,K=map(int,input().split())
    graph=[[] for _ in range(N)]
    for _ in range(K):
        u,v,c,d=map(int,input().split());u-=1;v-=1;
        graph[u].append((v,c,d))

    
    dists=[[INF]*(M+1) for _ in range(N)]
    dists[0][M]=0
    heap=deque()
    heap.append((0,0,M))

    while heap:
        d,cur,money=heap.popleft()
        if dists[cur][money]<d:
            continue

        for nextt,cost,dist in graph[cur]:
            if money-cost>=0 and dists[nextt][money-cost]>d+dist:
                dists[nextt][money-cost]=d+dist
                heap.append((dists[nextt][money-cost],nextt,money-cost))

    res=min(dists[N-1])
    print((res if res!=INF else "Poor KCM"))





#[print(ans) for ans in ansL]


#memory excess
from collections import defaultdict
from heapq import heappush,heappop
import math;INF=math.inf
import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())
ansL=[]


for _ in range(int(input())):
    N,M,K=map(int,input().split())
    graph=defaultdict(list)
    for _ in range(K):
        u,v,c,d=map(int,input().split());u-=1;v-=1;
        graph[u].append((v,c,d))

    
    dists=[dict() for _ in range(N)]
    for i in range(M+1):
        dists[0][i]=0

    heap=[]
    heappush(heap,(0,0,M))

    while heap:
        d,cur,money=heappop(heap)
        if dists[cur].get(money,INF)<d:
            continue

        for nextt,cost,dist in graph[cur]:
            if money-cost>=0 and dists[nextt].get(money-cost,INF)>d+dist:
                dists[nextt][money-cost]=d+dist
                heappush(heap,(dists[nextt][money-cost],nextt,money-cost))
    
    dists[N-1][-1]=INF
    res=min(dists[N-1].values())
    ansL.append(res if res!=INF else "Poor KCM")





[print(ans) for ans in ansL]



#best solution
#https://www.acmicpc.net/source/29239095
from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize

def solution():
    n, m, k = map(int, input().split())
    edges = [[] for _ in range(n+1)]
    dp = [[INF] * (m+1) for _ in range(n+1)]
    dp[1][0] = 0

    for _ in range(k):
        u, v, c, d = map(int, input().split())
        edges[u].append((v, c, d))
    
    q = deque([(1, 0, 0)])
    while q:
        node, c, d = q.popleft() # 노드, 비용, 거리
        if dp[node][c] < d: # 기존에 업데이트한 거리가 더 짧은 경우
            continue # 갱신하지 않음

        for next_node, next_c, next_d in edges[node]: # 다음 노드에 대해서
            cost = c + next_c # 이전 노드까지의 비용과 다음 노드로 가는 비용을 합친 지금까지 낸 금액
            dist = d + next_d # 이전 노드까지의 거리와 다음 노드로 가는 거리를 합친 지금까지 이동한 거리
            if cost > m or dp[next_node][cost] <= dist: # 예산 초과나 기존에 업데이트한 거리가 더 짧은 경우
                continue # 갱신하지 않음
            
            #key part
            # 갱신 시작
            for i in range(cost, m+1): # 현재 자본으로 갈 수 있는 거리 갱신
                # 다음 노드까지 갔을 때, 해당 자본으로 기존 이동한 거리보다 더 조금 이동하여 도착한다면
                if dp[next_node][i] > dist:
                    dp[next_node][i] = dist # 갱신
                else: # 더 큰 값을 지불한 이동 거리가 더 작다면
                    break
            q.append((next_node, cost, dist))

    print(dp[-1][-1] if dp[-1][-1] < INF else "Poor KCM")

T = int(input())
for _ in range(T):
    solution()