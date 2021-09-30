import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())

graph=[]
cameras=[] #[(type,(x,y))   ]
cameras5=[]
#making graph
for i in range(n):
    row = list(map(int,input().rstrip().split()))
    for j in range(m):
        if row[j]==5:
            cameras5.append((i,j))
        elif row[j]!=0 and row[j]!=6:
            cameras.append((row[j],(i,j)))
    graph.append(row)

#dealing with camear5
for x,y in cameras5:
    #look down:
    for i in range(x+1,n):
        if graph[i][y]==6:
            break
        graph[i][y]=7
    #look up
    if x!=0:
        for i in range(x-1,-1,-1):
            if graph[i][y]==6:
                break
            graph[i][y]=7
    #look right
    for i in range(y+1,m):
        if graph[x][i]==6:
            break
        graph[x][i]=7
    #look left
    if y!=0:
        for i in range(y-1,-1,-1):
            if graph[x][i]==6:
                break
            graph[x][i]=7



l=len(cameras)
def workCCTV(graph,type,x,y,dir):
    #look down:
    if  (type==1 and dir==0) or (type==2 and dir%2==1) or (type==3 and (dir==2 or dir==3)) or (type==4 and dir!=0):
        for i in range(x+1,n):
            if graph[i][y]==6:
                break
            graph[i][y]=7
    #look up
    if (type==1 and dir==2) or (type==2 and dir%2==1) or (type==3 and (dir==0 or dir==1)) or (type==4 and dir!=1):
        for i in range(x-1,-1,-1):
            if graph[i][y]==6:
                break
            graph[i][y]=7
    #look right
    if (type==1 and dir==1) or (type==2 and dir%2==0) or (type==3 and (dir==0 or dir==3)) or (type==4 and dir!=2):    
        for i in range(y+1,m):
            if graph[x][i]==6:
                break
            graph[x][i]=7
    #look left
    if (type==1 and dir==3) or (type==2 and dir%2==0) or (type==3 and (dir==2 or dir==1)) or (type==4 and dir!=3):
        if y!=0:
            for i in range(y-1,-1,-1):
                if graph[x][i]==6:
                    break
                graph[x][i]=7



def countNum(graph):
    num=0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                num+=1
    return num


maxNum=int(1e9)
for iter in range(4**l):
    tmp_graph=[]
    for row in graph:
        tmp_graph.append(row[:])

    for camera in cameras:
        dir = iter%4
        iter = iter//4
        workCCTV(tmp_graph,camera[0],camera[1][0],camera[1][1],dir)
    
    tmpNum=countNum(tmp_graph)
    #print(tmpNum,dir)
    if tmpNum==5:
        for row in tmp_graph:
            print(row)
        print("\n")
    maxNum =min(maxNum,tmpNum)

print(maxNum)