import sys
input=sys.stdin.readline

n=int(input())
budgets=list(map(int,input().rstrip().split()))
M=int(input())

if(sum(budgets)<=M):
    print(max(budgets))
    sys.exit()

le=1
ri=M
while le<ri:
    mid=(le+ri+1)//2
    totalSum=0
    for budget in budgets:
        if budget<mid:
            totalSum+=budget
        else:
            totalSum+=mid

    if totalSum>M:
        ri=mid-1
    elif totalSum==M:
        le=mid
    elif totalSum<M:
        le=mid

print(le)