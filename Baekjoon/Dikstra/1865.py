import sys
input = sys.stdin.readline
INF=int(1e9)

t = int(input())
ansList=[]


def bellman(start):
    global visited_num

    dist=[INF]*(n+1)
    dist[start]=0

    visited[start]=1
    visited_num+=1

    for i in range(n-1):
        for node in graph:
            for next_node in graph[node]:
                if dist[next_node] > dist[node]+graph[node][next_node]:
                    dist[next_node] = dist[node] + graph[node][next_node]

                    if visited[next_node]==0:
                        visited[next_node]=1
                        visited_num+=1
    
    for node in graph:
        for next_node in graph[node]:
            if dist[next_node] > dist[node]+graph[node][next_node]:
                return False


    #there is no loop
    return True


for _ in range(t):
    n,m,w = map(int,input().rstrip().split())
    graph={}
    answer="NO"

    visited= [0]*(n+1)
    visited_num=0
    visited[0]=1

    #creating roads
    for i in range(m+w):
        s,e,t = map(int,input().rstrip().split())

        #in case of wormhole
        if i>m-1:
            t = -t
        else:
            if e not in graph:
                graph[e]={s:t}
            elif s not in graph[e] or graph[e][s]>t:
                graph[e][s]=t

        if s not in graph:
            graph[s]={e:t}
        elif e not in graph[s] or graph[s][e]>t:
            graph[s][e]=t
        
    while visited_num!=n:
        start=0

        for i in range(1,n+1):
            if visited[i]==0:
                start=i
                break
        if not bellman(start):
            answer="YES"
            break
    
    ansList.append(answer)
            



for answer in ansList:
    print(answer)