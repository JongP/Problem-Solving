from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

v,e = map(int,input().rstrip().split())

#creating graph
fw = [[INF]*(v+1) for _ in range(v+1)]

for i in range(1,v+1):
    fw[i][i]=0

for _ in range(e):
    a,b,c = map(int,input().rstrip().split())
    if fw[a][b]>c:
        fw[a][b]=c
    
for k in range(1,v+1):
    for i in range(1,v+1):
        if i==k: continue
        for j in range(1,v+1):
            if fw[i][j] > fw[i][k]+fw[k][j]:
                fw[i][j] = fw[i][k]+fw[k][j]

answer=INF
for i in range(1,v+1):
    for j in range(1,v+1):
        if i==j: continue
        if fw[i][j]!=INF and fw[j][i]!=INF and answer>fw[i][j]+fw[j][i]:
            answer=fw[i][j]+fw[j][i]
if answer==INF:
    print(-1)
else:
    print(answer)
