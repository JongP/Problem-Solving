import sys
input=sys.stdin.readline

n,m=map(int,input().rstrip().split())
times=[]
for _ in range(n):
    times.append(int(input()))


times.sort()    

le=0
ri=times[-1]*m

while le<ri:
    mid=(le+ri)//2
    cnt=0
    for time in times:
        cnt+=mid//time
        
    if cnt>=m:
        ri=mid
    elif cnt<m:
        le=mid+1

print(le)
#print(ri) same