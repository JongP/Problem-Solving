from collections import deque
import sys
input=sys.stdin.readline
#map(int,input().rstrip().split())
#sys.setrecursionlimit(10**6)

n=int(input())

#left and right child of {node i}
leftN=[-2]*n
rightN=[-2]*n

#to find the root node
isChild=[False]*n

def getStack(leftN,rightN,root):
    stk=[]
    que=deque([root])
    stk=[root]
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

#-------------------build tree---------------#
for _ in range(n):
    p,l,r=map(int,input().rstrip().split())
    leftN[p-1]=l-1
    rightN[p-1]=r-1
    if l-1!=-2:
        isChild[l-1]=True
    if r-1!=-2:
        isChild[r-1]=True
    
for i in range(n):
    if not isChild[i]:
        root=i
        break


#----------------build dp-----------------#
dpLeft=[0]*n # dp[i]: number of node in left side of {node i}
dpRight=[0]*n# dp[i]: number of node in right side of {node i}
stk=getStack(leftN,rightN,root) #stack to travel from high level to low level

while stk:
    cur=stk.pop()
    l,r=leftN[cur],rightN[cur]
    if l!=-2:
        dpLeft[cur]=dpLeft[l]+dpRight[l]+1

    if r!=-2:
        dpRight[cur]=dpLeft[r]+dpRight[r]+1


que=deque([root]) #que to travel from low level to high level
while que:
    cur=que.popleft()
    l,r=leftN[cur],rightN[cur]
    if l!=-2:
        dpRight[l]+=dpRight[cur]+1
        que.append(l)
    if r!=-2:
        dpLeft[r]+=dpLeft[cur]+1
        que.append(r)

    
#------------------get maximum width and level----------------#
level=1
res=1
resLevel=1
lTrav,rTrav=leftN[root],rightN[root]

#최대한 바깥쪽으로 lTrav와 rTrav를 순회시킨다.
while lTrav!=-2 and rTrav!=-2:
    level+=1
    if res < dpLeft[rTrav] - dpLeft[lTrav] +1:
        res=dpLeft[rTrav] - dpLeft[lTrav] +1
        resLevel=level
    
    
    lTrav=leftN[lTrav] if leftN[lTrav]!=-2 else rightN[lTrav]
    rTrav=rightN[rTrav] if rightN[rTrav]!=-2 else leftN[rTrav]

print(resLevel,res)