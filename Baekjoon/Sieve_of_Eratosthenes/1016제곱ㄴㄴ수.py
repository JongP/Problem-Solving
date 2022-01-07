import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())
#sys.setrecursionlimit(10**5)

minN,maxN=map(int,input().split())

MAX=int(maxN**0.5)+1
dp=[True]*MAX
primes=[]
for i in range(2,MAX):
    if not dp[i]:
        continue
    primes.append(i)
    for j in range(i*i,MAX,i):
        dp[j]=False


s=set()
for p in primes:
    pp=p*p
    j=minN//pp
    while pp*j<=maxN:
        if minN<=pp*j and pp*j not in s:
            s.add(pp*j)
        j+=1

print(maxN-minN+1-len(s))