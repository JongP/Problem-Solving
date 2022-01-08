import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())
#sys.setrecursionlimit(10**5)

g=int(input())
res=[]
s=1
e=2
while s!=e:
    dif=e**2-s**2
    if dif>=g:
        if dif==g:
            res.append(e)
        s+=1
    else:
        e+=1

if res:
    [print(el) for el  in res]
else:
    print(-1)