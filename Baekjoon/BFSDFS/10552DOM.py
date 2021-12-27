import sys
input=sys.stdin.readline
n,m,p =map(int,input().rstrip().rsplit())

visited=[0]*m
graph=[-1]*m
for _ in range(n):
    a,b=map(int,input().rstrip().rsplit())
    if graph[b-1]==-1:
        graph[b-1]=a-1

prev=p-1
cnt=0
while True:
    visited[prev]=1
    nxt=graph[prev]
    if nxt==-1:
        break
    if  visited[nxt]==1:
        cnt=-1
        break
    cnt+=1
    prev=nxt



if cnt==-1:
    print(-1)
else:
    print(cnt)


#https://www.acmicpc.net/source/24361873
import sys
input =sys.stdin.readline

N,M,P = map(int,input().split())
graph=[0 for i in range(M+1)]
for _ in range(N):
    a,b = map(int,input().split())
    if not graph[b]:
        graph[b] = a


visited=[False for i in range(M+1)]

cnt=0
visited[P] = True
while graph[P] :
    visited[P] = True
    cnt+=1
    P=graph[P]
    if visited[P]:
        print(-1)
        exit()

print(cnt)