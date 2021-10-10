from collections import deque
import sys
input=sys.stdin.readline

answer=0

n,k = map(int,input().rstrip().split())

nameLens={}
for i in range(1,21):#1 is dummy value
    nameLens[i]=0

queue=[]
for _ in range(k):#k-1,k
    queue.append(1)

queue = deque(queue)

for _ in range(n):
    nameLen=len(input().rstrip())

    answer+=nameLens[nameLen]

    outLen=queue.popleft()
    queue.append(nameLen)
    nameLens[outLen]-=1
    nameLens[nameLen]+=1

print(answer)