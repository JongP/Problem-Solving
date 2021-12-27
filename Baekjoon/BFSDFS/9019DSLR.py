from collections import deque
import sys
input=sys.stdin.readline

class Node:
    def __init__(self,op=None,val=0,next=None):
        self.op=op
        self.val=val
        self.next=next

def printAnswer(node):
    tmp=""
    trav=node
    while trav.val!=a:
        #print(trav.val)
        tmp+=trav.op
        trav=trav.next

    ansL.append(tmp[::-1])#not tmp.reverse()




MAX=10000
ansL=[]
for _ in range(int(input())):
    visited=[0]*MAX
    a,b=map(int,input().rstrip().split())
    que=deque([Node(val=a)])
    visited[a]=1

    while que:
        cur=que.popleft()

        if cur.val==b:
            printAnswer(cur)
            break

        tmpS=str(cur.val)
        nD=(cur.val*2)%10000
        nS=cur.val-1 if cur.val!=0 else 9999
        nL=(cur.val*10)%10000+cur.val//1000 #if len(tmpS)!=1 else 
        nR=(cur.val)//10+(cur.val%10)*1000
        #D
        if nD<10000 and visited[nD]==0:
            que.append(Node("D",nD,cur))
            visited[nD]=1
        #S
        if visited[nS]==0:
            que.append(Node("S",nS,cur))
            visited[nS]=1
        #L
        if nL>=0 and nL<10000 and visited[nL]==0:
            que.append(Node("L",nL,cur))
            visited[nL]=1
        #R
        if nR>=0 and nR<10000 and visited[nR]==0:
            que.append(Node("R",nR,cur))
            visited[nR]=1

[print(a) for a in ansL]


#https://www.acmicpc.net/source/36462787
#you can just store the path in visited 
import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    
    visited = [""] * 10000
    idx = 0
    queue = [a]
    while 1:
        cur_node = queue[idx]
        idx += 1

        d = cur_node * 2 % 10000
        s = 9999 if cur_node == 0 else cur_node - 1
        l = (cur_node % 1000) * 10 + cur_node // 1000
        r = (cur_node % 10) * 1000 + cur_node // 10
        
        if d != a and not visited[d]:
            visited[d] = 'D1' if cur_node * 2 < 10000 else 'D2'
            if d == b: break
            queue.append(d)
            
        if s != a and not visited[s]:
            visited[s] = 'S'
            if s == b: break
            queue.append(s)
            
        if l != a and not visited[l]:
            visited[l] = 'L'
            if l == b: break
            queue.append(l)
            
        if r != a and not visited[r]:
            visited[r] = 'R'
            if r == b: break
            queue.append(r)

    ans = ""
    cur_node = b        
    while 1:
        if visited[cur_node] == 'D1':
            ans = 'D' + ans
            cur_node //= 2
        elif visited[cur_node] == 'D2':
            ans = 'D' + ans
            cur_node = (cur_node + 10000) // 2
        elif visited[cur_node] == 'S':
            ans = 'S' + ans
            cur_node = (cur_node + 1) % 10000
        elif visited[cur_node] == 'L':
            ans = 'L' + ans
            cur_node = cur_node // 10 + (cur_node % 10) * 1000
        elif visited[cur_node] == 'R':
            ans = 'R' + ans
            cur_node = (cur_node % 1000) * 10 + cur_node // 1000
        if cur_node == a: break
    
    print(ans)