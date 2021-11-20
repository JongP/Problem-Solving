import sys
input=sys.stdin.readline

n=int(input())

nums =[0]*(n+1)
graph={}

for _ in range(n):
    a,b = map(int,input().rstrip().split())

    nums[a]+=1
    nums[b]+=1

    if a not in graph:
        graph[a]=[b]
    else:
        graph[a].append(b)

    if b not in graph:
        graph[b]=[a]
    else:
        graph[b].append(a)


starts=[]
checkpoint=[]
for i in range(1,n+1):
    if nums[i]==1:
        starts.append(i)
    elif nums[i]>2:
        checkpoint.append(i)
ansList = [0]*(n+1)

def distAtoB(a,b):
    len=0
    pprev=a
    prev=a
    while True:
        for i in graph[prev]:
            if i==pprev: continue
            pprev=prev
            prev=i
            len+=1
            if i in b: return len
            break

def ansListUpdate(a,b,len):
    pprev=a
    prev=a
    while True:
        ansList[prev]=len
        for i in graph[prev]:
            if i == pprev: continue
            pprev=prev
            prev=i
            len-=1
            if i in b: return
            break

for start in starts:
    len = distAtoB(start,checkpoint)
    ansListUpdate(start,checkpoint,len)


print(ansList[1:])