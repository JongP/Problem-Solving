import sys
input=sys.stdin.readline


N,M= map(int,input().rstrip().split())
board=[list(map(int,input().rstrip().split())) for _ in range(N)]

ansL=[]

#input process
prefixSum=[[0]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        prefixSum[i][j]=prefixSum[i-1][j]+prefixSum[i][j-1]-prefixSum[i-1][j-1]+board[i-1][j-1]


#cal 
for _ in range(M):
    x1,y1,x2,y2 =map(int,input().rstrip().split())
    ansL.append(prefixSum[x2][y2]-prefixSum[x2][y1-1]-prefixSum[x1-1][y2]+prefixSum[x1-1][y1-1])




[print(a) for a in ansL]