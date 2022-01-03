import sys
input=lambda: sys.stdin.readline().rstrip()

#map(int,input().split())

g=int(input())
p=int(input())

parent=[i for i in range(g+1)]

def find(a):
    if parent[a]==a or parent[a]==0:
        return parent[a]
    
    parent[a]=find(parent[a])
    return parent[a]

def land(a):
    a=find(a)
    if a==0:
        return False
    
    parent[a]=parent[a-1]
    return True

res=0
for _ in range(p):
    plane=int(input())
    if not land(plane):
        break
    res+=1

for _ in range(p-res-1):
    input()

print(res)