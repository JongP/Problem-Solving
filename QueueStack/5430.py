from collections import deque
import sys
input=sys.stdin.readline

t=int(input())

ansList=[]
for _ in range(t):
    p=input().rstrip()
    n=int(input())
    if n!=0:
        numList=list(input().rstrip()[1:-1].split(","))
    else:
        input()
        numList=[]
    
    queue=deque(numList)
    isREV=False
    isERROR=False

    for operator in p:
        if operator=="R":
            isREV=not isREV
            continue

        if not queue:
            isERROR=True
            break

        if not isREV:
            queue.popleft()
        else:
            queue.pop()
        

    if isERROR:
        ansList.append("error")
        continue

    if isREV:
        queue.reverse()
    ansList.append("["+",".join(queue)+"]")
    
    
    





for answer in ansList:
    print(answer)