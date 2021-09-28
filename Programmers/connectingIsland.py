#https://programmers.co.kr/learn/courses/30/lessons/42861
def solution(n, costs):
    answer =0
    costs.sort(key = lambda x: x[2],reverse=True)

    firstA,firstB, firstCost = costs[-1]
    answer+=firstCost
    #최저 같을 case
    visited =set([firstA,firstB])

    graph ={}
    for a,b,cost in costs:
        if a not in graph:
            graph[a] = {b:cost}
        else:
            graph[a][b]=cost
        
        if b not in graph:
            graph[b] = {a:cost}
        else:
            graph[b][a]=cost


    while(len(visited)!=n):
        min_dest=-1
        min_cost=int(1e9)

        for visited_node in visited:
            for dest in graph[visited_node]:
                if dest in visited: continue
                if graph[visited_node][dest]<min_cost:
                    min_cost=graph[visited_node][dest]
                    min_dest=dest

        visited.add(min_dest)
        answer+=min_cost
    
    
    return answer



print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
