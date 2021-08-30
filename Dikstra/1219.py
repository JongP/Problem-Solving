import sys
input = sys.stdin.readline
INF = int(1e9)

n,a,b,m = map(int,input().rstrip().split())
graph={}
dist = [INF]*n

def isReachableToB(start):
    visited=[0]*n
    q=[start]

    while q:
        node = q.pop()
        if visited[node] ==1: continue
        else : visited[node]=1
        if node==b: return True

        if node not in graph: continue

        for next_node in graph[node]:
            if visited[next_node] ==0:
                q.append(next_node)
    return False

#creating graph
for _ in range(m):
    s,t,c = map(int,input().rstrip().split())

    if s not in graph:
        graph[s] = {t:c}
    elif t not in graph[s] or graph[s][t]>c:
        graph[s][t]=c

earnings = list(map(int,input().rstrip().split()))


#setting start
dist[a]=-1*earnings[a]

for _ in range(n-1):
    for node in graph:
        if dist[node]==INF: continue
        for next_node in graph[node]:
            if dist[next_node] > dist[node] + graph[node][next_node] - earnings[next_node] :
                dist[next_node] = dist[node] + graph[node][next_node] - earnings[next_node]
 
flag=False
if dist[b] == INF:
    print("gg")
else:
    for node in graph:
        if dist[node]==INF: continue
        for next_node in graph[node]:
            if dist[next_node] > dist[node] + graph[node][next_node] - earnings[next_node]:
                dist[next_node] = dist[node] +graph[node][next_node] - earnings[next_node]
                if isReachableToB(next_node):
                    flag=True
                    break
        if flag: break
    if flag:
        print("Gee")
    else:    
        print(-1*dist[b])


