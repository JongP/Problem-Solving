
import copy
INF=int(1e9)
def floyd(n):
    global floyd_table
    floyd_table=copy.deepcopy(graph)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if floyd_table[i][k]+floyd_table[k][j]<floyd_table[i][j]:
                    floyd_table[i][j]=floyd_table[i][k]+floyd_table[k][j]
    for row in floyd_table:
        print(row)




def solution(n, s, a, b, fares):
    answer = INF
    global floyd_table,graph

    graph=[[INF]*n for _ in range(n)]
    for i in range(n):
        graph[i][i]=0

    for c,d,f in fares:
        graph[c-1][d-1]=f
        graph[d-1][c-1]=f

    floyd(n)

    s-=1
    a-=1
    b-=1

    for i in range(n):
        answer=min(answer,floyd_table[s][i]+floyd_table[i][b]+floyd_table[i][a])

    return answer

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))