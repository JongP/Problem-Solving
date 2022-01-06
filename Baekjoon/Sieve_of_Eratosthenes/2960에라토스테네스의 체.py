import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())
#sys.setrecursionlimit(10**5)

n,k=map(int,input().split())

era=[True]*(n+1)

for i in range(2,n+1):
    if not era[i]:
        continue
    era[i]=False
    k-=1
    if k==0:
        print(i)
        exit()
    for j in range(i*i,n+1,i):
        if era[j]:
            k-=1
            era[j]=False
            if k==0:
                print(j)
                exit()