import sys
input=lambda : sys.stdin.readline().rstrip()


n=int(input())
m=int(input())
edges=sorted([list(map(int,input().split())) for _ in range(m) ],key= lambda x:x[2])

parents=[-1]*n
def find(x):
    if parents[x]<0:
        return x
    parents[x]=find(parents[x])
    return parents[x]

def union(x,y):
    x=find(x)
    y=find(y)
    if x==y:
        return False
    
    parents[x]+=parents[y]
    parents[y]=x

    return True


res=0
idx=0
for a,b,c in edges:
    if idx==n-1:
        break
    
    if union(a-1,b-1):
        idx+=1
        res+=c

print(res)


