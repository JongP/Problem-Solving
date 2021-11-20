from collections import deque
import sys
ip=sys.stdin.readline

f,s,g,u,d = tuple(map(int,ip().rstrip().split()))

visited = [0]*(f+1)
found=False

if s==g:
    queue =None
    found=True
else: 
    queue = deque([s])
    visited[s]=1

res=0

while queue:
    l = len(queue)
    res+=1
    for _ in range(l):
        cur=queue.popleft()

        if cur-d>0 and visited[cur-d]==0:
            queue.append(cur-d)
            visited[cur-d]=1
        if cur+u<=f and visited[cur+u]==0:
            queue.append(cur+u)
            visited[cur+u]=1
        
        if g==cur-d or g==cur+u:
            queue=None
            found=True
            break

if found:
    print(res)
else:
    print("use the stairs")