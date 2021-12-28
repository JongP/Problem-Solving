#unsolved!!!

from copy import deepcopy
n=10
graph=[list(map(int,input().split()))for _ in range(10)]
leftP=[0,5,5,5,5,5]
numOne=sum([line.count(1) for line in graph])
if numOne==0:
    print(0)
    exit()
res=int(2e9)
cnt=0

def setPlace(graph,x,y,size,flag):
    if x+size>=n or y+size>=n:
        return False
    for i in range(size):
        for j in range(size):
            graph[x+i][y+j]=0 if flag else 1
    return True
    

def place(graph,leftP,x,y,depth):
    global res,cnt,numOne
    if cnt==numOne:
        if res<depth:
            res=depth
        return

    while x<n:
        while y<n:
            if graph[x][y]==0:
                y+=1
                continue
            for i in range(1,6):
                if setPlace(graph,x,y,i,True) and leftP[i]>0:
                    leftP[i]-=1
                    cnt+=i
                    place(graph,leftP,x,y,depth+1)
                    setPlace(graph,x,y,i,False)
                    leftP[i]+=1
                    cnt-=i
            y+=1
        y=0
        x+=1



place(graph,leftP,0,0,1)

        


res=-1 if res==int(2e9) else res
print(res)