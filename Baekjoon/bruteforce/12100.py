#https://www.acmicpc.net/source/28279505
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

graph=[]
for _ in range(n):
    graph.append(list(map(int,input().rstrip().split())))

def PrintGraph(graph):
    return
    for row in graph:
        print(row)
def PrintTest(graph):
    for row in graph:
        print(row)

def go_right(graph,depth):
    global maxNum
    
    #actual move
    newGraph=[]
    for row in graph:
        newRow =[0]*n
        queue = deque([])
        
        #오른 끝 붙이기
        j=n-1
        for i in range(n-1,-1,-1):
            if row[i]!=0:
                if queue and queue[-1][0]==row[i] and queue[-1][1]==0:
                    queue.pop()
                    queue.append((2*row[i],1))
                else:
                    queue.append((row[i],0))
        for i in range(n-1,-1,-1):
            if not queue:
                break
            num, _ = queue.popleft()
            newRow[i]= num

        newGraph.append(newRow)


    if depth==4:
        tmp_max=0
        for row in newGraph:
            for num in row:
                tmp_max=max(tmp_max,num)
        maxNum = max(maxNum,tmp_max)
        PrintGraph(newGraph)
        return

    go_right(newGraph,depth+1)
    go_left(newGraph,depth+1)
    go_up(newGraph,depth+1)
    go_down(newGraph,depth+1)       

def go_left(graph,depth):
    global maxNum
    
    #actual move
    newGraph=[]
    for row in graph:
        newRow =[0]*n
        queue = deque([])
        
        #오른 끝 붙이기
        j=n-1
        for i in range(n):
            if row[i]!=0:
                if queue and queue[-1][0]==row[i] and queue[-1][1]==0:
                    queue.pop()
                    queue.append((2*row[i],1))
                else:
                    queue.append((row[i],0))
        for i in range(n):
            if not queue:
                break
            num, _ = queue.popleft()
            newRow[i]= num

        newGraph.append(newRow)

    if depth==4:
        tmp_max=0
        for row in newGraph:
            for num in row:
                tmp_max=max(tmp_max,num)
        maxNum = max(maxNum,tmp_max)
        PrintGraph(newGraph)
        return

    go_right(newGraph,depth+1)
    go_left(newGraph,depth+1)
    go_up(newGraph,depth+1)
    go_down(newGraph,depth+1)   

def go_up(graph,depth):
    global maxNum
    
    #actual move
    newGraph=[[0]*n for _ in range(n)]

    for i in range(n):
        queue = deque([])
        
        #오른 끝 붙이기
        for j in range(n):
            if graph[j][i]!=0:
                if queue and queue[-1][0]==graph[j][i] and queue[-1][1]==0:
                    queue.pop()
                    queue.append((2*graph[j][i],1))
                else:
                    queue.append((graph[j][i],0))
        for j in range(n):
            if not queue:
                break
            num, _ = queue.popleft()
            newGraph[j][i]= num

    if depth==4:
        tmp_max=0
        for row in newGraph:
            for num in row:
                tmp_max=max(tmp_max,num)
        maxNum = max(maxNum,tmp_max)
        PrintGraph(newGraph)
        return

    go_right(newGraph,depth+1)
    go_left(newGraph,depth+1)
    go_up(newGraph,depth+1)
    go_down(newGraph,depth+1) 

def go_down(graph,depth):
    global maxNum
    
    #actual move
    newGraph=[[0]*n for _ in range(n)]

    for i in range(n):
        queue = deque([])
        
        #오른 끝 붙이기
        for j in range(n-1,-1,-1):
            if graph[j][i]!=0:
                if queue and queue[-1][0]==graph[j][i] and queue[-1][1]==0:
                    queue.pop()
                    queue.append((2*graph[j][i],1))
                else:
                    queue.append((graph[j][i],0))
        for j in range(n-1,-1,-1):
            if not queue:
                break
            num, _ = queue.popleft()
            newGraph[j][i]= num

    if depth==4:
        tmp_max=0
        for row in newGraph:
            for num in row:
                tmp_max=max(tmp_max,num)
        maxNum = max(maxNum,tmp_max)
        PrintGraph(newGraph)
        return
    
    go_right(newGraph,depth+1)
    go_left(newGraph,depth+1)
    go_up(newGraph,depth+1)
    go_down(newGraph,depth+1)

maxNum=0

go_right(graph,0)
go_left(graph,0)
go_down(graph,0)
go_up(graph,0)

print(maxNum)