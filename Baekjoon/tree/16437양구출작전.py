from collections import defaultdict
import sys
input=sys.stdin.readline
#map(int,input().rstrip().split())
sys.setrecursionlimit(123556)
n=int(input())
aList=[0]*(n+1)
tList=[""]*(n+1)
graph=defaultdict(list)

iNum=2
for _ in range(n-1):
    t,a,p=input().rstrip().split()
    a,p=map(int,(a,p))
    aList[iNum]=a
    tList[iNum]=t
    graph[p].append(iNum)
    iNum+=1

#print(tList,aList,graph)

def postorder(node):

    incoming=0
    for nxt in graph[node]:
        incoming+=postorder(nxt)

    if tList[node]=="W":
        incoming=incoming-aList[node] if incoming-aList[node]>=0 else 0
    else:
        incoming+=aList[node]

    return incoming


print(postorder(1))
