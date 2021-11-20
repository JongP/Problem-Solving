import sys 
input = sys.stdin.readline

r,c= map(int,input().rstrip().split())

graph = [list(input().rstrip()) for _ in range(r)]


def DFS(x,y):
    global graph
    graph[x][y]='X'

    if(y==c-1):
        return True
    
    if x!=0 and graph[x-1][y+1]=='.' and DFS(x-1,y+1):
        return True
    elif graph[x][y+1]=='.' and DFS(x,y+1):
        return True
    elif x!=r-1 and graph[x+1][y+1]=='.' and DFS(x+1,y+1):
        return True
    else:
        #graph[x][y]='.' 하면 안됨. 어차피 길 없음.
        return False

answer=0
##위에서 아래로
for i in range(r):
    if DFS(i,0):
        answer+=1
    




print(answer)