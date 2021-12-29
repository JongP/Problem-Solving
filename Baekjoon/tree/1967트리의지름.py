from collections import defaultdict
import sys
input=sys.stdin.readline

sys.setrecursionlimit(10**5)
#map(int,input().rstrip().split())

n=int(input())
graph=defaultdict(list)


for _ in range(n-1):
    a,b,w=map(int,input().rstrip().split())
    graph[a].append((b,w))

res=0
def postorder(node):
    global res


    tmp=[0,0]
    for nxt,w in graph[node]:
        tmp.append(postorder(nxt))
        tmp[-1]+=w
    tmp.sort()
    if res<tmp[-1]+tmp[-2]:
        res=tmp[-1]+tmp[-2]

    return max(tmp)

postorder(1)
print(res)