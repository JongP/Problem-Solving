#important issue is whether you recognize that this can be solved with binary search or not
#remember bianry search is parrametric search! you can come up with this approach
#brute force takes too long! --> binary search
import sys
input=sys.stdin.readline
N,K,D=map(int,input().rstrip().split())
rules=[list(map(int,input().rstrip().split())) for _ in range(K)]

le=1
ri=1000000

def getVal(n):
    res=0
    for a,b,c in rules:
        if a>n:
            continue
        res+=(min(n,b)-a)//c+1
    return res

while le<ri:
    mid=(le+ri)//2
    val=getVal(mid)
    if val>=D:
        ri=mid
    else:

        le=mid+1


print(le)