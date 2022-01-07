import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())
#sys.setrecursionlimit(10**5)


a,b=map(int,input().split())

maxN=10**7+1
dp=[True]*maxN 
primes=[]
for i in range(2,maxN):
    if not dp[i]:
        continue
    if i*i>b:
        break

    primes.append(i)
    for j in range(i*i,maxN,i):
        dp[j]=False       
res=0
for p in primes:
    j=2
    tmp=p**2
    while tmp<=b:
        if a<=tmp:
            res+=1
        tmp*=p

print(res)


#https://www.acmicpc.net/source/31296975
#VARIANCE of sieve of eratosthenes
min, max = map(int, input().split())

chk = [1] * (max - min + 1)
# 2부터 max의 제곱근 수까지만 체크하면 충분.
for n in range(2, int(max ** 0.5) + 1):
    square = n ** 2
    i = min // square
    # 제곱수의 배수가 min보다 크도록 나눈몫+1해줌.
    # 거기서부터 쭉 i증가시키며 돌고 n번째 수 다 끝나면 다음 n으로 넘어가며 check배열에 0으로 바꿔줌.
    if square * i < min:
        i += 1
    while square * i <= max:
        chk[square * i - min] = 0
        i += 1
print(sum(chk))