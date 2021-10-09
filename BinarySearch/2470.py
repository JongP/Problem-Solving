import sys
input=sys.stdin.readline

n=int(input())
liquids=sorted(list(map(int,input().rstrip().split())))


minSum=int(2e9)

#exception
if liquids[-1]<=0:
    print(liquids[-2],liquids[-1])
    sys.exit()
if liquids[0]>=0:
    print(liquids[0],liquids[1])
    sys.exit()

le=0
ri=n-1
while le<ri:
    mixSum=liquids[le]+liquids[ri]
    if abs(mixSum)<minSum:
        answer=(liquids[le],liquids[ri])
        minSum=abs(mixSum)
    
    if mixSum<0:
        le+=1
    elif mixSum==0:
        break
    else:
        ri-=1



print(answer[0],answer[1])