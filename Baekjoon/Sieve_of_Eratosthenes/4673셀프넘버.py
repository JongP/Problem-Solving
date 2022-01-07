import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())
#sys.setrecursionlimit(10**5)
MAX=10000+1
dp=[False]*MAX

for i in range(1,MAX):
    if dp[i]:
        continue
    print(i)
    
    while i<MAX:
        if dp[i]:
            break
        dp[i]=True
        tmp=i
        while i:
            i,r=divmod(i,10)
            tmp+=r
        i=tmp
        
