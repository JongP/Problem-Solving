from collections import defaultdict
import sys
input=lambda: sys.stdin.readline().rstrip()

#map(int,input().split())
#sys.setrecursionlimit(10**5)


def find(a):
    if a not in p:
        p[a]=""
        return a
    elif len(p[a])==0:
        return a

    p[a]=find(p[a])#wonderful mistake you will never make again
    return p[a]

def union(a,b):
    a=find(a)
    b=find(b)
    if a==b:
        return
    s[a]+=s[b]
    p[b]=a

ansL=[]
tt=int(input())
for _ in range(tt):
    p={}
    s=defaultdict(lambda:1)
    for _ in range(int(input())):
        a,b=input().split()
        union(a,b)
        ansL.append(s[find(a)])


[print(a) for a in ansL]