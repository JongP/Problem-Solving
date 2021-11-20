import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().rstrip().split())

floyd = [[INF]*(n+1) for _ in range(n+1)]


#creating graph
for _ in range(m):
    a,b = map(int,input().rstrip().split())
    
    floyd[a][b]=1

#floyd-washal
for i in range(1,n+1):
    floyd[i][i]=0
    for j in range(1,n+1):
        if j==i: continue
        for k in range(1,n+1):
            if k==i: continue
            if floyd[j][k]> floyd[j][i]+floyd[i][k]:
                floyd[j][k]= floyd[j][i]+floyd[i][k]


answer=0
#validating whether it can make order
for i in range(1,n+1):
    isI = True
    for j in range(1,n+1):
        if floyd[i][j]==INF and floyd[j][i]==INF:
            isI=False
            break

    if isI:
        answer+=1 

print(answer)