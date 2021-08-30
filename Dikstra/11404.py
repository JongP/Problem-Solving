import sys
input = sys.stdin.readline
from math import inf
INF=inf

n=int(input())
m=int(input())

graph={}

floid = [[INF]*(n+1) for _ in range(n+1)]
for i in range(n+1):
    floid[i][i]=0

for _ in range(m):
    a,b,c = map(int,input().rstrip().split())
    
    floid[a][b]=min(floid[a][b],c)


for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            # j->k vs j->i->k
            if floid[j][k]>floid[j][i]+floid[i][k]:
                floid[j][k]=floid[j][i]+floid[i][k]

for i in range(1,n+1):
    row_string=""
    for j in range(1,n+1):
        num=floid[i][j]
        if num==INF: num=0
        row_string+=str(num)+" "
    print(row_string.rstrip())
