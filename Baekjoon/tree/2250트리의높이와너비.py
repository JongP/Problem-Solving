from collections import deque
import sys
input=sys.stdin.readline
#map(int,input().rstrip().split())
#sys.setrecursionlimit(10**6)

n=int(input())

leftN=[-2]*n
rightN=[-2]*n

def getStack(leftN,rightN):
    stk=[]
    que=deque([0])
    stk=[0]
    while que:
        cur=que.popleft()
        #print(cur)
        if leftN[cur]!=-2:
            que.append(leftN[cur])
            stk.append(leftN[cur])

        if rightN[cur]!=-2:
            que.append(rightN[cur])
            stk.append(rightN[cur])

    return stk

for _ in range(n-1):
    p,l,r=map(int,input().rstrip().split())
    leftN[p-1]=l-1
    rightN[p-1]=r-1

#root=0

#build dp
dpLeft=[0]*n

stk=getStack(leftN,rightN)

while stk:
    cur=stk.pop()
    l,r=leftN[cur],rightN[cur]

    if l!=-2:
        dp[cur]+=dp[l]+1

    if r!=-2:
        dp[r]+=dp[cur]+1

    

level=1
res=0
resLevel=1
lTrav,rTrav=leftN[0],rightN[0]
print(dp)
while lTrav!=-2 and rTrav!=-2:
    level+=1
    if res < dp[rTrav] - dp[lTrav] +1:
        res=dp[rTrav] - dp[lTrav] +1
        resLevel=level
    
    
    lTrav=leftN[lTrav] if leftN[lTrav]!=-2 else rightN[lTrav]
    rTrav=rightN[rTrav] if rightN[rTrav]!=-2 else leftN[rTrav]

print(resLevel,res)