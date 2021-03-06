import sys
input=sys.stdin.readline

t = int(input())

zeros=[-1]*41
ones=[-1]*41
ansList=[]

zeros[0]=1;ones[0]=0
zeros[1]=0;ones[1]=1

for _ in range(t):
    n=int(input())
    if zeros[n]==-1:
        for i in range(n+1):
            if zeros[i]!=-1:
                continue
            zeros[i]=zeros[i-1]+zeros[i-2]
            ones[i]=ones[i-1]+ones[i-2]
    ansList.append((zeros[n],ones[n]))


for zero,one in ansList:
    print(zero,one)

