MOD=1000000007
def solution(m, n, puddles):
    answer = 0

    roads=[[0]*m for _ in range(n)]
    roads[0][0]=1

    for puddle in puddles:
        roads[puddle[1]-1][puddle[0]-1]=-1
    

    for i in range(1,m+n-1):
        for j in range(i+1):
            #print(i,j,i-j)
            if j>=m or i-j<0 or i-j>=n:
                continue
             #from left to right
            if roads[i-j][j]==-1:
                continue

            
            if j!=0 and roads[i-j][j-1]!=-1:
                roads[i-j][j]= (roads[i-j][j]+roads[i-j][j-1])%MOD

            if i-j!=0 and roads[i-j-1][j]!=-1:
                roads[i-j][j]= (roads[i-j][j]+roads[i-j-1][j])%MOD
            
            #    roads[i-j][j]+= roads[i-j-1][j]
            #    roads[i-j][j]%MOD
            #this doesnt work.

            #print(roads)
            #from up to down

    
    print(roads[n-1][m-1])
    return roads[n-1][m-1]