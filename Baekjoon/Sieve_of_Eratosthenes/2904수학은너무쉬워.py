#소인수 분해 비슷한거

import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())
#sys.setrecursionlimit(10**5)

n=int(input())
nums=list(map(int,input().split()))
maxN=max(nums)+1
rest=0
res=1

dp=[True]*maxN
primes=[]
for i in range(2,maxN):
    if not dp[i]:
        continue
    primes.append(i)
    for j in range(i*i,maxN,i):
        dp[j]=False


for prime in primes:
    arr=[]
    s=0
    for num in nums:
        tmp=0
        while num>=prime and num%prime==0:
            num//=prime
            tmp+=1
        arr.append(tmp)
        s+=tmp
    
    t=s//len(arr)
    res*=prime**t
    for e in arr:
        if e<t:
            rest+=t-e

print(res,rest)


#소인수 분해 툴 배우자
#https://www.acmicpc.net/source/13528060
def f(n): #소인수분해
    t=2
    d={}
    while t*t<=n:
        if n%t==0:
            d[t]=d.get(t,0)+1
            n=n//t
        else:
            t+=1
    if n>1:
        d[n]=d.get(n,0)+1
    return d

n=int(input())
l=list(map(int,input().split()))
avgd={} #평균 소인수

for i in l:
    tempd=f(i) #l안의 수 하나 소인수분해
    for j in tempd:
        avgd[j]=avgd.get(j,0)+tempd[j]

for i in avgd: #최대공약수의 소인수들
    avgd[i]=avgd[i]//n

r1=1 #점수
r2=0 #시행횟수
for i in avgd:
    r1*=i**avgd[i] #최대공약수

for i in l:
    temp=f(i)
    for j in avgd:
        if avgd[j]>temp.get(j,0):
            r2+=avgd[j]-temp.get(j,0)

print("%d %d"%(r1,r2))