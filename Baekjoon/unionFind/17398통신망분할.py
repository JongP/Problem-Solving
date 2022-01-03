#just wow
import sys
input=lambda: sys.stdin.readline().rstrip()

#map(int,input().split())
#sys.setrecursionlimit(10**5)

n,m,q=map(int,input().split())
edges=[list(map(lambda x:int(x)-1,input().split())) for _ in range(m)]
que=[int(input())-1 for _ in range(q)]
que.reverse()
queS=set(que)
#print(edges,que)

p=[-1]*n
res=0

def find(node):
    if p[node]<0:
        return node

    p[node]=find(p[node])
    return p[node]

def union(a,b,flag):
    global res#I dont need this actually
    a=find(a)
    b=find(b)

    if a==b:
        return
    if flag:
        res+=p[a]*p[b]
    p[a]+=p[b]
    p[b]=a

#initial setting
for i in range(m):
    if i in queS:
        continue
    union(edges[i][0],edges[i][1],False)


#let's go back
for i in que:
    a,b=edges[i]
    union(a,b,True)

print(res)



def find(x):
    if head[x] == x:
        return x
    head[x] = find(head[x])
    return head[x]

def union(a, b):
    if a < b:
        head[b] = a
        counter[a] += counter[b]
    else:
        head[a] = b
        counter[b] += counter[a]
        

#https://www.acmicpc.net/source/35302011
N, M, Q = map(int, input().split())
sun = [tuple(map(int, input().split())) for _ in range(M)]
head = [x for x in range(N+1)]
counter = [1]*(N+1)
ch = [0]*(M)
remove= []
for _ in range(Q):
    idx = int(input())
    ch[idx-1] = 1
    remove.append(idx-1)

for i in range(M):
    if ch[i] == 1: continue
    a, b = find(sun[i][0]),find(sun[i][1])
    if a != b: 
        union(a, b)
res = 0
for r in remove:
    a, b = find(sun[r][0]), find(sun[r][1])
    if a != b:
        res += counter[a] * counter[b]
        union(a, b)
print(res)