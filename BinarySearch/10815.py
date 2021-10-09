import sys
input = sys.stdin.readline

n=int(input())
nList=list(map(int,input().rstrip().split()))
nList.sort()


m=int(input())
mList=list(map(int,input().rstrip().split()))

answer=[]

for target in mList:
    le=0
    ri=n-1
    while le<=ri:
        mid = (le+ri)//2
        if nList[mid]>target:
            ri=mid-1
        elif nList[mid]<target:
            le=mid+1
        else:
            answer.append("1")
            break
    if le>ri:
        answer.append("0")

print(" ".join(answer))