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

#https://www.acmicpc.net/source/28193275

t = int(input())

import sys

input = sys.stdin.readline
def find(a):
    if parent[a] == a:
        return a, 0
    current = 0
    if dist[a] == 0:
        current += abs(a-parent[a]) % 1000
    p, parent_dist = find(parent[a])
    current += parent_dist
    dist[a] += current

    parent[a] = p
    return parent[a],dist[a]


for _ in range(t):
    n = int(input())

    parent = list(range(n + 1))
    dist = [0] * (n + 1)
    while True:
        lst = input().split()
        if lst[0] == 'O':
            break

        op = lst[0]

        if op == 'E':
            a= int(lst[1])
            if dist[a] == 0:
                find(a)
                print(dist[a])
            else:
                p,d = find(a)
                print(dist[a])

        else:
            a, b = int(lst[1]), int(lst[2])

            parent[a] = b
