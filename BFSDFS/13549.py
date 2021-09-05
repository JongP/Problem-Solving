from collections import deque
import sys
input = sys.stdin.readline
MAX= 100000
INF = int(1e9)

n,k = map(int,input().rstrip().split())
if n==k:
    print(0)
    sys.exit()

visited=[INF]*(MAX+1)

queue = deque([n])
visited[n] = 0


while queue:
    l = len(queue)

    for _ in range(l):
        cur = queue.popleft()
        sec = visited[cur]
        if 2*cur<=MAX and visited[2*cur]>sec:
            visited[2*cur] = sec
            queue.append(2*cur)
        if cur>0 and visited[cur-1]>sec+1:
            visited[cur-1] = sec+1
            queue.append(cur-1)
        if cur<MAX and visited[cur+1]>sec+1:
            visited[cur+1] = sec+1
            queue.append(cur+1)



print(visited[k])