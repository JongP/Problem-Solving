from collections import deque
import sys
input = sys.stdin.readline
MAX= 100000

n,k = map(int,input().rstrip().split())
if n==k:
    print(0)
    print(n)
    sys.exit()

visited=[-1]*(MAX+1)

queue = deque([n])
visited[n] = n

sec=0
while queue:
    l = len(queue)

    for _ in range(l):
        cur = queue.popleft()
        if cur>0 and visited[cur-1]==-1:
            visited[cur-1] = cur
            queue.append(cur-1)
        if cur<MAX and visited[cur+1]==-1:
            visited[cur+1] = cur
            queue.append(cur+1)
        if 2*cur<=MAX and visited[2*cur]==-1:
            visited[2*cur] = cur
            queue.append(2*cur)
    sec+=1
    
    if k in queue:
        break

track=k
tracks=[str(k)]
while track!=n:
    track=visited[track]
    tracks.append(str(track))
tracks.reverse()

print(sec)
print(" ".join(tracks))