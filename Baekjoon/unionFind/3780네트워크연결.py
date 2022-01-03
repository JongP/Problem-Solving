#please remind me of  this again
import sys
input=lambda: sys.stdin.readline().rstrip()

#map(int,input().split())
#sys.setrecursionlimit(10**5)

def find(x):
    if p[x]==x:
        return x
    elif p[p[x]]==p[x]:
        return p[x]
    tmp=p[x]
    p[x]=find(p[x])
    dists[x]=dists[x]+dists[tmp]
    return p[x]

def union(c,n):
    nC=find(n)

    dists[c]=dists[n]+abs(n-c)%1000
    p[c]=nC

for _ in range(int(input())):
    n=int(input())
    p=[i for i in range(n)]
    dists=[0]*n

    line =input()
    while line!="O":
        ops=line.split()

        if ops[0]=="I":
            center,node=int(ops[1])-1,int(ops[2])-1
            union(center,node)

        else:
            node=int(ops[1])-1
            find(node)
            print(dists[node])


        line=input()


