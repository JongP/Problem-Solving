import sys
input= sys.stdin.readline

L,N,rF,rB= map(int,input().rstrip().split())
gap=rF-rB
stops=[]

for _ in range(N):
    stops.append(list(map(int,input().rstrip().split())))

stops.reverse()

print(stops)

cache=[L,0]
res=0
for x,c in stops:
    tmpRes= x*gap*c+(cache[0]-x)*gap*cache[1]

    if tmpRes>res:
        res=tmpRes
        cache[0]=x
        cache[1]=c

print(res)