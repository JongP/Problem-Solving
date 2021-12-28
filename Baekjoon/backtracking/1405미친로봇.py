N,e,w,s,n =map(int,input().split())
e,w,s,n=e/100,w/100,s/100,n/100
probs=[e,w,s,n]
dxdy=((0,1,0),(1,-1,0),(2,0,1),(3,0,-1))
res=0
visited=set()

def makeMovement(x,y,prob,k):
    global res
    visited.add((x,y))
    if k==0:
        res+=prob
        return

    for i,dx,dy in dxdy:
        nX,nY=x+dx,y+dy
        if (nX,nY) not in visited and probs[i]:
            makeMovement(nX,nY,prob*probs[i],k-1)
            visited.remove((nX,nY))


makeMovement(0,0,1,N)
print(res)

#https://www.acmicpc.net/source/15206733
def dfs(r, c, p, a):
    global k
    if arr[r][c]==1:
        k += p
        return
    if a == N:
        return
    if e:
        arr[r][c] = 1
        dfs(r,c+1,p*e,a+1)
        arr[r][c] = 0
    if w:
        arr[r][c] = 1
        dfs(r,c-1,p*w,a+1)
        arr[r][c] = 0
    if s:
        arr[r][c] = 1
        dfs(r+1,c,p*s,a+1)
        arr[r][c] = 0
    if n:
        arr[r][c] = 1
        dfs(r-1,c,p*n,a+1)
        arr[r][c] = 0

N, e, w, s, n = map(int, input().split())
e, w, s, n = e/100, w/100, s/100, n/100
arr = [[0 for _ in range(29)] for _ in range(29)] #the map is not that large. this optimize the time
cnt = 0
k = 0
dfs(14, 14, 1, cnt)
print('{:.10f}'.format(1-k))