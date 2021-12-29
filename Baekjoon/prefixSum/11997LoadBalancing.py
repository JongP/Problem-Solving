#hint: coordination compaction
import sys
input=sys.stdin.readline

n=int(input())
cows=[list(map(int,input().rstrip().split())) for _ in range(n)]

#compact the coordination
for _ in range(2):
    cows.sort()
    compactedX=-1
    prv=None
    for cow in cows:
        if cow[0]==prv:
            cow[0]=compactedX
        else:
            compactedX+=1
            prv=cow[0]
            cow[0]=compactedX
        cow[0],cow[1]=cow[1],cow[0]

yard=[[0]*(n+1) for _ in range(n+1)]
for a,b in cows:
    yard[a][b]=1

#process prefixSum
prefixSum=[[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        prefixSum[i][j]=prefixSum[i-1][j]+prefixSum[i][j-1]-prefixSum[i-1][j-1]+yard[i-1][j-1]


#find the minimum M
M=int(2e9)
for i in range(1,n+1):
    for j in range(1,n+1):
        tmp=max(max(prefixSum[i][j],prefixSum[n][n]-prefixSum[n][j]-prefixSum[i][n]+prefixSum[i][j])\
            ,max(prefixSum[i][n]-prefixSum[i][j],prefixSum[n][j]-prefixSum[i][j]))
        if tmp<M:
            M=tmp
print(M)
#[print(cow) for cow in cows]