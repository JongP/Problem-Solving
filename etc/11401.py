import sys
input=sys.stdin.readline

N,K = map(int,input().rstrip().split())


#n!/k!/(n-k)!
answer=1


#n!/(n-k)!
for i in range(N-K+1,N+1):
    answer*=i

for i in range(1,K+1):
    answer//=i

print(int(answer)%1000000007)