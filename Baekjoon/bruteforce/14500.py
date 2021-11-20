import sys
input = sys.stdin.readline


n,m=map(int,input().rstrip().split())

graph=[]
for _ in range(n):
    graph.append(list(map(int,input().rstrip().split())))

# 1x4 4x1 2x3 3x2 2x2
maxNum=0
for i in range(n):
    for j in range(m):
        #1x4
        if j<m-3:
            maxNum=max(maxNum,graph[i][j]+graph[i][j+1]+graph[i][j+2]+graph[i][j+3])
        #4x1
        if i<n-3:
            maxNum=max(maxNum,graph[i][j]+graph[i+1][j]+graph[i+2][j]+graph[i+3][j])
        #3x2
        if i<n-2 and j<m-1:
            maxNum=max(maxNum,graph[i][j]+graph[i+1][j]+graph[i+2][j]+graph[i+1][j+1])
            maxNum=max(maxNum,graph[i][j+1]+graph[i+1][j+1]+graph[i+2][j+1]+graph[i+1][j])

            maxNum=max(maxNum,graph[i][j]+graph[i+1][j]+graph[i+1][j+1]+graph[i+2][j+1])
            maxNum=max(maxNum,graph[i][j+1]+graph[i+1][j+1]+graph[i+1][j]+graph[i+2][j])

            maxNum=max(maxNum,graph[i][j]+graph[i+1][j]+graph[i+2][j]+graph[i][j+1])
            maxNum=max(maxNum,graph[i][j]+graph[i+1][j]+graph[i+2][j]+graph[i+2][j+1])

            maxNum=max(maxNum,graph[i][j+1]+graph[i+1][j+1]+graph[i+2][j+1]+graph[i][j])
            maxNum=max(maxNum,graph[i][j+1]+graph[i+1][j+1]+graph[i+2][j+1]+graph[i+2][j])
        #2x3
        if i<n-1 and j<m-2:
            maxNum=max(maxNum,graph[i][j]+graph[i][j+1]+graph[i][j+2]+graph[i+1][j+1])
            maxNum=max(maxNum,graph[i+1][j]+graph[i+1][j+1]+graph[i+1][j+2]+graph[i][j+1])

            maxNum=max(maxNum,graph[i][j]+graph[i][j+1]+graph[i+1][j+1]+graph[i+1][j+2])
            maxNum=max(maxNum,graph[i+1][j]+graph[i+1][j+1]+graph[i][j+1]+graph[i][j+2])

            maxNum=max(maxNum,graph[i][j]+graph[i][j+1]+graph[i][j+2]+graph[i+1][j+2])
            maxNum=max(maxNum,graph[i][j]+graph[i][j+1]+graph[i][j+2]+graph[i+1][j])
            
            maxNum=max(maxNum,graph[i+1][j]+graph[i+1][j+1]+graph[i+1][j+2]+graph[i][j+2])
            maxNum=max(maxNum,graph[i+1][j]+graph[i+1][j+1]+graph[i+1][j+2]+graph[i][j])

        #2x2
        if i<n-1 and j<m-1:
            maxNum=max(maxNum,graph[i][j]+graph[i][j+1]+graph[i+1][j]+graph[i+1][j+1])

print(maxNum)