import sys
input = sys.stdin.readline


n, m = tuple(map(int,input().rstrip().split()))
graph = {}
visited = [0]*n
visited_num=0
stack=[]
res=0

#creating graph
for _ in range(m):
    n1,n2 = tuple(map(int,input().rstrip().split()))

    if n1 not in graph:
        graph[n1]=[n2]
    else:
        graph[n1].append(n2)
    
    if n2 not in graph:
        graph[n2]=[n1]
    else:
        graph[n2].append(n1)


while visited_num!=n:
    #when stack is empty
    if len(stack)==0: #not stack works?
        for i in range(n):
            if visited[i]==0:
                stack.append(i+1)
                res+=1
                break
        continue
    
    num = stack.pop()
    
    visited[num-1]=1
    visited_num+=1

    if num not in graph:
        continue

    for adj in graph[num]:
        if visited[adj-1]==0:
            stack.append(adj)

print(res)