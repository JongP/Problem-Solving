import sys
input=sys.stdin.readline

n,l=map(int,input().rstrip().split())

numbers =[list(map(int,input().rstrip().split())) for _ in range(n)]

def canGo(road):
    flatRoad=1
    prevRoad=road[0]
    step=[0]*n

    for i in range(1,n):
        if abs(prevRoad-road[i])>1:
            return 0
        elif road[i]-prevRoad==1:#go up
            if flatRoad<l or step[i-1]==1:
                return 0
            flatRoad=1
            prevRoad=road[i]
        elif road[i]-prevRoad==-1: #go down
            if i> n-l:
                return 0
            for j in range(i+1,i+l):
                if road[j]!=road[i]:  return 0
                step[j]=1

            flatRoad=0
            prevRoad=road[i]
        elif step[i]==0:
            flatRoad+=1
    #print(road)
    return 1

answer =0

for row in numbers:
    answer+=canGo(row)
for i in range(n):
    row=[]
    for j in range(n):
        row.append(numbers[j][i])
    answer+=canGo(row)

print(answer)
#print(canGo([3,3,3,3,2,2]))